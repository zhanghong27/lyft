from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_sensor):
        self.wear_sensor = wear_sensor

    def needs_service(self):
        sum = 0
        for i in self.wear_sensor:
            sum += i
        if sum >= 3:
            return True
        return False