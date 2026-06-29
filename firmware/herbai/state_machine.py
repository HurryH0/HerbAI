"""
HerbAI guided state machine.

This is the real control flow that drives the on-screen experience. Hardware reads/writes
go through the sensors/ and actuators/ modules (which carry TODOs for your specific parts),
so this logic is testable on a laptop with simulated readings.
"""

from enum import Enum, auto
from . import recipes
from .config import TDS_TOLERANCE_PPM, MIN_SAFE_LEVEL_FRACTION


class State(Enum):
    BOOT = auto()
    WAIT_WATER = auto()     # ask the user to fill the reservoir
    SELECT_CROP = auto()    # choose one of the 5 herbs
    DOSING = auto()         # guide the user to the stage's target ppm
    GROWING = auto()        # day-by-day; nudge to feed at stage transitions
    HEALTH = auto()         # camera check + recipe update
    HARVEST = auto()


class Controller:
    def __init__(self, sensors, actuators, ui):
        self.sensors = sensors
        self.actuators = actuators
        self.ui = ui
        self.state = State.BOOT
        self.crop = None
        self.stage_index = 0
        self.day_in_stage = 0

    # --- helpers ---------------------------------------------------------
    @property
    def stage(self):
        return recipes.stages_for(self.crop)[self.stage_index]

    def _has_water(self):
        return self.sensors.tof.level_fraction() > MIN_SAFE_LEVEL_FRACTION

    def _dissolved_mass(self):
        """Sensor fusion: level (volume proxy) x concentration ~= dissolved nutrient mass."""
        return self.sensors.tof.level_fraction() * self.sensors.tds.read_ppm()

    # --- one tick of the loop -------------------------------------------
    def step(self):
        if self.state is State.BOOT:
            self.ui.splash("HerbAI")
            self.state = State.WAIT_WATER

        elif self.state is State.WAIT_WATER:
            if self._has_water():
                self.ui.message("Water detected. Add seeds, then choose a crop.")
                self.state = State.SELECT_CROP
            else:
                self.ui.prompt_fill_water()

        elif self.state is State.SELECT_CROP:
            choice = self.ui.choose_crop()           # blocks until the user taps one
            if choice:
                self.crop = choice
                self.stage_index = 0
                self.day_in_stage = 0
                self.state = State.DOSING

        elif self.state is State.DOSING:
            target = self.stage.ppm_target
            current = self.sensors.tds.read_ppm()
            self.ui.dosing_guide(current, target, TDS_TOLERANCE_PPM)
            if abs(current - target) <= TDS_TOLERANCE_PPM:
                self.ui.message(f"On target for {self.stage.stage}. Growing!")
                self.state = State.GROWING

        elif self.state is State.GROWING:
            self.actuators.pump.recirculate(enabled=self._has_water())
            self.ui.show_stage(self.crop, self.stage, self.day_in_stage)
            self.day_in_stage += 1
            if self.day_in_stage % 2 == 0:           # periodic canopy check
                self.state = State.HEALTH
            elif self.day_in_stage >= self.stage.days:
                self._advance_stage()

        elif self.state is State.HEALTH:
            self.actuators.stepper.move_camera_to_canopy()
            frame = self.sensors.camera.capture()
            status = self.sensors.camera.assess(frame)   # healthy / yellowing / curling
            self.ui.show_health(status)
            # mass dropping => real uptake => nudge to feed; rising-but-flat-mass => evaporation
            self.state = State.GROWING

        elif self.state is State.HARVEST:
            self.ui.message("Harvest time. Enjoy — grown on a fraction of the water.")

    def _advance_stage(self):
        stages = recipes.stages_for(self.crop)
        if self.stage_index + 1 < len(stages):
            self.stage_index += 1
            self.day_in_stage = 0
            self.ui.nudge_add_nutrient(self.stage)    # "next stage — add nutrient"
            self.state = State.DOSING
        else:
            self.state = State.HARVEST
