"""Actuator interfaces (pump, stepper)."""
from .pump import Pump
from .stepper import Stepper


class Actuators:
    def __init__(self):
        self.pump = Pump()
        self.stepper = Stepper()

    def shutdown(self):
        self.pump.recirculate(enabled=False)
        self.stepper.disable()
