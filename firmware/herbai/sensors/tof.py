"""ToF water-level sensor (VL53L0X) in the reservoir."""
from ..config import RESERVOIR_EMPTY_DISTANCE_MM, RESERVOIR_FULL_DISTANCE_MM


class ToF:
    def read_distance_mm(self) -> float:
        # TODO: read VL53L0X range here.
        raise NotImplementedError("wire up VL53L0X read here")

    def level_fraction(self) -> float:
        """0.0 (empty) .. 1.0 (full). Closer surface = more water."""
        try:
            d = self.read_distance_mm()
        except NotImplementedError:
            d = 90  # simulated mid-level for desktop testing
        span = RESERVOIR_EMPTY_DISTANCE_MM - RESERVOIR_FULL_DISTANCE_MM
        frac = (RESERVOIR_EMPTY_DISTANCE_MM - d) / span
        return max(0.0, min(1.0, frac))
