"""Hardware configuration. Set these to match YOUR build before flashing."""

# --- Reservoir geometry (used for sensor fusion + dose maths) ---
RESERVOIR_VOLUME_L = 2.0          # litres at "full"
RESERVOIR_EMPTY_DISTANCE_MM = 180 # ToF distance reading when empty
RESERVOIR_FULL_DISTANCE_MM = 40   # ToF distance reading when full
MIN_SAFE_LEVEL_FRACTION = 0.12    # pump is disabled below this (dry-run protection)

# --- TDS / EC ---
TDS_SCALE = 500                   # ppm conversion scale (500 / 640 / 700). We standardise on 500.
TDS_TOLERANCE_PPM = 40            # "within target" band shown as green in the UI

# --- GPIO pins (BCM numbering) — PLACEHOLDERS, edit me ---
PIN_PUMP_RELAY = 17
PIN_STEPPER_STEP = 23
PIN_STEPPER_DIR = 24
PIN_STEPPER_EN = 25

# --- Crops available in the UI menu ---
CROPS = ["mint", "basil", "coriander", "oregano", "spring_onion"]
