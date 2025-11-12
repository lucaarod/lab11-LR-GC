# https://github.com/lucaarod/lab11-LR-GC
# Partner 1: Luca Rodriguez
# Partner 2: Guilherme Carvalheira

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): 
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 8), -5)
        self.assertAlmostEqual(subtract(2.5, 0.5), 2.0)

    ######## Partner 1
    def test_multiply(self): 
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertAlmostEqual(mul(2.5, 2), 5.0)

    def test_divide(self): 
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        self.assertEqual(div(-9, 3), -3)

    ######## Partner 2
    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): 
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(0.5, 0.25), 2.0)

    def test_log_invalid_base(self):  
        with self.assertRaises(ValueError):
            log(1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(-5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()