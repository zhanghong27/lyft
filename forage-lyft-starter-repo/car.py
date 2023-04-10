from engine_base import Engine

from battery_base import Battery

from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
