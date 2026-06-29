"""Stepper-driven lead screw that raises/lowers the camera over the canopy."""
from ..config import PIN_STEPPER_STEP, PIN_STEPPER_DIR, PIN_STEPPER_EN


class Stepper:
    def __init__(self):
        self.position = 0
        # TODO: GPIO.setup STEP/DIR/EN pins

    def move_camera_to_canopy(self):
        """Park the camera at a fixed height so image scale is consistent across a batch
        (consistent scale -> real leaf-area growth curves)."""
        # TODO: step to the calibrated canopy position.
        self.position = 1

    def disable(self):
        # TODO: GPIO.output(PIN_STEPPER_EN, GPIO.HIGH)  # de-energise coils
        pass
