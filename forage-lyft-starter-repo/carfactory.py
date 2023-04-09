from abc import ABC

from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory(ABC):
    def create_calliope(self, current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(engine= CapuletEngine, battery= SpindlerBattery)
    
    def create_glissade(self, current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(engine= WilloughbyEngine, battery= SpindlerBattery)
    
    def create_palindrome(self, current_date,last_service_date, warming_light_is_on):
        return Car(engine= SternmanEngine, battery= SpindlerBattery)
        
    def create_rorschach(self, current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(engine= WilloughbyEngine, battery= NubbinBattery)

    def create_thovex(self, current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(engine= CapuletEngine, battery= NubbinBattery)