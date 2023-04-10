import sys
import os
sys.path.append(os.path.abspath("/Users/zhanghong/Desktop/web_project/theForage_LYFT/forage-lyft-starter-repo"))
from engine_base import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
