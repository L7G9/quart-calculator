import unittest
from calculator_service.calculator import Calculator

class Test(unittest.TestCase):
    def setUp(self):
       self.calculator = Calculator()
       self.list = [4,5,1,2,3]

    def test_add(self):
        self.assertEqual(self.calculator.add(20, 10), 30)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(20, 10), 200)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(20, 10), 2)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(self.list), 15)

    def test_mean(self):
        self.assertEqual(self.calculator.mean(self.list), 3)
