# Hardware (bill of materials)

All off-the-shelf and low-cost. Exact parts can be swapped; roles are what matter.

| Part | Role |
|------|------|
| Raspberry Pi Zero W (or Zero 2 W) | Main controller / UI / light ML inference. Zero 2 W recommended if running on-device CV. |
| SPI TFT display (e.g. ILI9341, 2.8") | Guided user interface — prompts, ppm, water level, stage. |
| TDS / EC probe (analog) + ADS1115 ADC | Measures nutrient concentration in the reservoir. |
| ToF distance sensor (VL53L0X) | Measures water level (distance to surface) in the reservoir. |
| Submersible / peristaltic pump (5–12 V) | Recirculates solution from reservoir to planter. |
| Relay module (or MOSFET) | Switches the pump (and optional grow light). |
| Stepper motor (28BYJ-48 / NEMA-17) + driver (ULN2003 / A4988) | Drives the lead-screw camera mount. |
| Lead screw + nut + linear guide | Raises/lowers the camera over the canopy. |
| USB camera (e.g. Logitech C270, 720p) | Canopy imaging for plant-health / recipe learning. |
| Rockwool cubes (5×5 grid) | Soilless growing medium. |
| 2 L reservoir + tubing + overflow standpipe | Closed recirculating loop. |
| 3D-printed enclosure + side covers | Vase form factor; hides electronics; structural taper. |

## Wiring notes

- TDS probe is analog → read via ADS1115 (I²C). Apply temperature compensation if a water-temp
  sensor (e.g. DS18B20) is fitted.
- VL53L0X is I²C; mount it under the planter pointing at the reservoir water surface.
- Pump relay and stepper STEP/DIR pins are defined in
  [`firmware/herbai/config.py`](../firmware/herbai/config.py).

> ⚠️ Pin numbers in `config.py` are placeholders — set them to match your build before flashing.
