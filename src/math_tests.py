import calc
import unittest

class TestMathLibrary(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(2, 2), 4)
        self.assertEqual(calc.add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 2), -1)
        self.assertEqual(calc.subtract(2, 2), 0)
        self.assertEqual(calc.subtract(3, 2), 1)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 2), 2)
        self.assertEqual(calc.multiply(2, 2), 4)
        self.assertEqual(calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(1, 2), 0.5)
        self.assertEqual(calc.divide(2, 2), 1)
        self.assertEqual(calc.divide(3, 2), 1.5)

    def test_power(self):
        self.assertEqual(calc.power(1, 2), 1)
        self.assertEqual(calc.power(2, 2), 4)
        self.assertEqual(calc.power(3, 2), 9)
    
    def test_root(self):
        self.assertEqual(calc.root(1, 2), 1)
        self.assertEqual(calc.root(4, 2), 2)
        self.assertEqual(calc.root(9, 2), 3)

    def test_factorial(self):
        self.assertEqual(calc.factorial(1), 1)
        self.assertEqual(calc.factorial(2), 2)
        self.assertEqual(calc.factorial(3), 6)

    def test_logarithm(self):
        self.assertEqual(calc.logarithm(1, 2), 0)
        self.assertEqual(calc.logarithm(2, 2), 1)
        self.assertEqual(calc.logarithm(3, 2), 1.5849625007211563)
