from datetime import datetime

from car import Car

from engine.capuletengine import CapuletEngine
from engine.willoughbyengine import WilloughbyEngine
from engine.sternmanengine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire



class CarFactory():
    current_date = datetime.now.date()

    def createCallope(last_service_mileage,current_mileage,last_service_date,current_date,tire_wear):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine,battery,tire)
        return car
    
    def createGlissade(last_service_mileage,current_mileage,last_service_date,current_date,tire_wear):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine,battery,tire)
        return car
    
    def createPalindrome(warning_light_on,last_service_date,current_date,tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine,battery,tire)
        return car
    
    def createRorschach(last_service_mileage,current_mileage,last_service_date,current_date,tire_wear):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine,battery,tire)
        return car
    
    def createThovex(last_service_mileage,current_mileage,last_service_date,current_date,tire_wear):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine,battery,tire)
        return car