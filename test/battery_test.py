from unittest import TestCase
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
import datetime as dt

class TestNubbinBattery(TestCase):
    def test_needservice(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2019,4,1)
        battery= NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_needservice2(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2018,4,1)
        battery= NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())
    
    def test_no_needservice(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2021,4,1)
        battery= NubbinBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(TestCase):
    def test_needservice(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2017,4,1)
        battery= SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())

    def test_needservice2(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2018,4,1)
        battery= SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.needs_service())
    
    def test_no_needservice(self):
        current_date = dt.datetime.now().date()
        last_service_date = dt.date(2021,4,1)
        battery= SpindlerBattery(last_service_date,current_date)
        self.assertFalse(battery.needs_service())

