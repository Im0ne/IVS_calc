
from math_lib import MathLib as calc
import unittest

class TestMathLibrary(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(2, 2), 4)
        self.assertEqual(calc.add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(calc.sub(1, 2), -1)
        self.assertEqual(calc.sub(2, 2), 0)
        self.assertEqual(calc.sub(3, 2), 1)
    
    def test_multiply(self):
        self.assertEqual(calc.mul(1, 2), 2)
        self.assertEqual(calc.mul(2, 2), 4)
        self.assertEqual(calc.mul(3, 2), 6)

    def test_divide(self):
        self.assertEqual(calc.div(1, 2), 0.5)
        self.assertEqual(calc.div(2, 2), 1)
        self.assertEqual(calc.div(3, 2), 1.5)

    def test_power(self):
        self.assertEqual(calc.pow(1, 2), 1)
        self.assertEqual(calc.pow(2, 2), 4)
        self.assertEqual(calc.pow(3, 2), 9)
    
    def test_root(self):
        self.assertEqual(calc.root(1, 2), 1)
        self.assertEqual(calc.root(4, 2), 2)
        self.assertEqual(calc.root(8, 3), 2)

    def test_factorial(self):
        self.assertEqual(calc.fact(1), 1)
        self.assertEqual(calc.fact(2), 2)
        self.assertEqual(calc.fact(3), 6)

    def test_absolute(self):
        self.assertEqual(calc.abs(1), 1)
        self.assertEqual(calc.abs(-1), 1)
        self.assertEqual(calc.abs(-235233), 235233)
    
    def test_modulo(self):
        self.assertEqual(calc.mod(1, 2), 1)
        self.assertEqual(calc.mod(2, 2), 0)
        self.assertEqual(calc.mod(3, 2), 1)
