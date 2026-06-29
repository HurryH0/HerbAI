"""TDS / EC probe (analog, read via an ADS1115 ADC)."""
from ..config import TDS_SCALE


class TDS:
    def read_voltage(self) -> float:
        # TODO: read the ADS1115 channel wired to the TDS probe.
        raise NotImplementedError("wire up ADS1115 read here")

    def read_ppm(self) -> int:
        """Return concentration in ppm on the configured scale.

        Replace the body with your calibrated voltage->ppm curve. A simulated value is
        returned here so the UI/state machine run on a laptop.
        """
        try:
            v = self.read_voltage()
            # TODO: calibrated polynomial, with temperature compensation if available.
            return int(v * TDS_SCALE)
        except NotImplementedError:
            return 320  # simulated tap-water-ish reading for desktop testing
