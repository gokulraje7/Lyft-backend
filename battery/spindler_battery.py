from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.spindler_needs_service = 3


    def needs_service(self):
        return self.current_date-self.last_service_date > self.spindler_needs_service 
        