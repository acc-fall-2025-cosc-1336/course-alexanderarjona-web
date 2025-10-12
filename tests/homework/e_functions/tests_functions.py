#import unittest
from src.homework.e_functions.value_return_functions import (
    get_gross_pay, get_fica_tax, get_federal_tax
)

class TestPayrollFunctions(unittest.TestCase):

    def test_get_gross_pay_no_overtime(self):
        self.assertAlmostEqual(get_gross_pay(40, 10), 400)

    def test_get_gross_pay_with_overtime(self):
        self.assertAlmostEqual(get_gross_pay(45, 10), 475)

    def test_get_gross_pay_less_than_40(self):
        self.assertAlmostEqual(get_gross_pay(30, 10), 300)

    def test_get_fica_tax(self):
        self.assertAlmostEqual(get_fica_tax(400), 30.6, places=2)

    def test_get_federal_tax(self):
        self.assertAlmostEqual(get_federal_tax(400), 32.0, places=2)

if __name__ == "__main__":
    unittest.main()
