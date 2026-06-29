"""Recirculating pump on a relay. Dry-run protection is enforced by the caller (ToF level)."""
from ..config import PIN_PUMP_RELAY


class Pump:
    def __init__(self):
        self._on = False
        # TODO: GPIO.setup(PIN_PUMP_RELAY, GPIO.OUT)

    def recirculate(self, enabled: bool):
        """Enable/disable recirculation. Consider intermittent (ebb-and-flow) duty cycling
        so roots get oxygen between floods."""
        self._on = enabled
        # TODO: GPIO.output(PIN_PUMP_RELAY, GPIO.HIGH if enabled else GPIO.LOW)
