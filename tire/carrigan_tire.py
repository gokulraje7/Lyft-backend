from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear
        self.carrigan_need_service = 0.9

    def needs_service(self):
        return self.tire_wear >= self.carrigan_need_service
