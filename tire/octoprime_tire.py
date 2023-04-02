from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear
        self.octoprime_need_service = 3

    def needs_service(self):
        return self.tire_wear >= self.octoprime_need_service
