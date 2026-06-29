"""Sensor interfaces. Real hardware reads are marked TODO; defaults let you run on a laptop."""
from .tds import TDS
from .tof import ToF
from .camera import Camera


class Sensors:
    def __init__(self):
        self.tds = TDS()
        self.tof = ToF()
        self.camera = Camera()
