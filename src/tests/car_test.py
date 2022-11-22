import unittest
from sprites.car import Car

class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car()
    
    def test_car_setup(self):
        self.assertEqual(self.car.speed, 0)