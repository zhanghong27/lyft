from car import Car

from abc import ABC

class Serviceable(ABC):
    def needs_service(self):
        pass