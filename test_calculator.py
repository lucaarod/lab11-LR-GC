import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(3, 8), -5)
        self.assertAlmostEqual(sub(2.5, 0.5), 2.0)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 1000), 3.0)
        self.assertAlmostEqual(log(0.5, 0.25), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()