#

import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(3), 6)
        self.assertEqual(get_factorial(1), 1)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(5), 9)
        self.assertEqual(sum_odd_numbers(10), 25)
        self.assertEqual(sum_odd_numbers(1), 1)

if __name__ == "__main__":
    unittest.main()
