import sys
import os
sys.path.append(os.path.abspath("/Users/zhanghong/Desktop/web_project/theForage_LYFT/forage-lyft-starter-repo"))
from engine_base import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
