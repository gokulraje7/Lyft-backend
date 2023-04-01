from datetime import datetime

from car import Car

from engine.capuletengine import CapuletEngine
from engine.willoughbyengine import WilloughbyEngine
from engine.sternmanengine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery



class CarFactory():
    current_date = datetime.now.date()

    def createCallope(last_service_mileage,current_mileage,last_service_date,current_date):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    def createGlissade(last_service_mileage,current_mileage,last_service_date,current_date):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    def createPalindrome(warning_light_on,last_service_date,current_date):
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    def createRorschach(last_service_mileage,current_mileage,last_service_date,current_date):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car
    
    def createThorex(last_service_mileage,current_mileage,last_service_date,current_date):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        car = Car(engine,battery)
        return car