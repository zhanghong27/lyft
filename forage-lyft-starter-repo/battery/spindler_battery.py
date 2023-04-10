import sys
import os
sys.path.append(os.path.abspath("/Users/zhanghong/Desktop/web_project/theForage_LYFT/forage-lyft-starter-repo"))
from battery_base import Battery
from utils import add_years_to_date


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 2)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
