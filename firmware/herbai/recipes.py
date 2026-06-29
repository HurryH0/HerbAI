"""
Per-crop nutrient recipes by growth stage.

Targets are EC (mS/cm) and the equivalent ppm on the 500 scale. These are sensible
STARTING POINTS for leafy herbs — calibrate against your own water and results, and let the
recipe-learning layer (see ../../ml) refine them per crop over successive batches.

pH matters as much as EC: keep the solution around 5.5–6.5 for all of these crops.
"""

from dataclasses import dataclass


@dataclass
class StageTarget:
    stage: str
    days: int          # nominal days in this stage
    ec_min: float      # mS/cm
    ec_max: float      # mS/cm
    ppm_target: int    # 500-scale, mid of range — what the UI guides toward


# Generic leafy-herb schedule; per-crop overrides below.
_BASE = [
    StageTarget("seedling",   3, 0.4, 0.8, 300),   # start near plain water, ramp gently
    StageTarget("vegetative", 14, 1.0, 1.4, 600),
    StageTarget("mature",     10, 1.2, 1.6, 700),
]

RECIPES = {
    "mint":         _BASE,
    "coriander":    _BASE,
    "oregano":      _BASE,
    "spring_onion": [
        StageTarget("seedling",   4, 0.5, 0.9, 350),
        StageTarget("vegetative", 16, 1.2, 1.6, 700),
        StageTarget("mature",     12, 1.4, 1.8, 800),
    ],
    "basil": [
        StageTarget("seedling",   3, 0.5, 0.9, 350),
        StageTarget("vegetative", 14, 1.1, 1.6, 650),
        StageTarget("mature",     10, 1.4, 1.8, 800),
    ],
}


def stages_for(crop: str):
    """Return the ordered list of StageTarget for a crop."""
    return RECIPES.get(crop, _BASE)


def target_ppm(crop: str, stage: str) -> int:
    for s in stages_for(crop):
        if s.stage == stage:
            return s.ppm_target
    raise ValueError(f"unknown stage {stage!r} for crop {crop!r}")
