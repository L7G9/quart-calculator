import unittest
from calculator_service.calculator import Calculator


class Test(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.odd_list = [5, 2, 1, 4, 3]
        self.even_list = [5, 4, 3, 2, 1, 6]
        self.no_mode_list = [5, 2, 3, 1, 6, 4]
        self.single_mode_list = [5, 2, 3, 5, 4, 3, 5, 1, 2, 5]
        self.multiple_mode_list = [5, 4, 1, 5, 4, 5, 3, 2, 3, 6, 3, 1]


    def test_add(self):
        self.assertEqual(self.calculator.add(20, 10), 30)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(20, 10), 10)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(20, 10), 200)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(20, 10), 2)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(self.odd_list), 15)

    def test_mean(self):
        self.assertEqual(self.calculator.mean(self.odd_list), 3)

    def test_odd_median(self):
        self.assertEqual(self.calculator.median(self.odd_list), 3)

    def test_event_median(self):
        self.assertEqual(self.calculator.median(self.even_list), 3.5)

    def test_no_mode(self):
        result = self.calculator.mode(self.no_mode_list)
        self.assertEqual(len(result), 0)

    def test_single_mode(self):
        result = self.calculator.mode(self.single_mode_list)
        self.assertEqual(result[0], 5)

    def test_multiple_mode(self):
        result = self.calculator.mode(self.multiple_mode_list)
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], 3)
