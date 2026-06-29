"""HerbAI entry point. Run on the Raspberry Pi: `python -m herbai.main`."""

import time

from .state_machine import Controller
from .sensors import Sensors
from .actuators import Actuators
from .ui import UI


def main(tick_seconds: float = 1.0):
    sensors = Sensors()
    actuators = Actuators()
    ui = UI()
    controller = Controller(sensors, actuators, ui)

    try:
        while True:
            controller.step()
            time.sleep(tick_seconds)
    except KeyboardInterrupt:
        actuators.shutdown()


if __name__ == "__main__":
    main()
