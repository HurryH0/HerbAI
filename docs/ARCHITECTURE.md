# Architecture

HerbAI is a recirculating (ebb-and-overflow) hydroponic system with a guided UI and a
closed sensing/dosing loop.

## Water path

```
        ┌──────────── planter (rockwool grid) ────────────┐
        │   overflow standpipe sets the water level       │
        └─▲───────────────────────────────────────┬───────┘
   supply │ (pump lifts solution up)      return  │ (excess drains down)
        ┌─┴───────────────────────────────────────▼───────┐
        │            2 L reservoir (nutrient solution)     │
        │   pump · ToF level sensor · TDS concentration    │
        └──────────────────────────────────────────────────┘
```

- **Supply (up):** the pump lifts solution from the reservoir to the planter.
- **Return / overflow (down):** an overflow standpipe holds a fixed level in the planter and
  returns everything above it to the reservoir. Water never leaves the loop.

## Control loop

```
sensors ──▶ state machine ──▶ UI (TFT) ──▶ user action
   ▲                │
   │                ▼
   └──── pump / stepper actuators
```

## Sensor fusion: telling evaporation from uptake

A small reservoir drifts fast, so a single reading is ambiguous. We combine the two cheap
sensors we already have:

```
dissolved_mass ≈ level (ToF)  ×  concentration (TDS)
```

- concentration **rises** but mass **holds** → evaporation → prompt a plain-water top-up.
- mass **drops** → the plant is feeding → time to dose.

This turns two ~₹100 sensors into a real measurement of what the crop is actually drinking,
and makes the saving visible to the user.

## States

`BOOT → WAIT_WATER → SELECT_CROP → DOSING → GROWING(seedling→vegetative→mature) → HEALTH → HARVEST`

See [`firmware/herbai/state_machine.py`](../firmware/herbai/state_machine.py).

## Safety

- **Dry-run protection:** the pump is enabled only while ToF reports water above a minimum,
  so an empty 2 L reservoir can never burn it out.
- **Dose limits:** dosing guidance is calibrated to the 2 L volume; the UI guides in small
  increments toward the stage target rather than dumping nutrient.
