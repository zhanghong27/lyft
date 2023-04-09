from abc import ABC, abstractmethod

from engine_base import Engine

from battery_base import Battery

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
