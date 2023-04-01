from unittest import TestCase

from engine.capuletengine import CapuletEngine
from engine.sternmanengine import SternmanEngine
from engine.willoughbyengine import WilloughbyEngine

class TestCapuletEngine(TestCase):
    def test_capulet_need_service(self):
        current_mileage = 30030
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())
    def test_no_need_service(self):
        current_mileage = 65000
        last_service_mileage = 30000
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())
class TestWilloughbyEngine(TestCase):
    def test_willoughby_need_service(self):
        current_mileage = 75000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())
    def test_willoughby_no_need_service(self):
        current_mileage = 75000
        last_service_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())
class TestSternmanEngine(TestCase):
    def test_sternmanengine_need_service(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())
    def test_sternman_no_need_service(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())