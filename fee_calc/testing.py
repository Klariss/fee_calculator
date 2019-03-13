import unittest
from calculator import FeeCalc, LoanData, Term


class TestFeeCalc(unittest.TestCase):

    def test_less_than_1000_value(self):
        """ Testing whether value errors raised when less than 1000 loan value is given. """
        arg1 = LoanData(loan=100, term=Term.TERM_12)
        calc = FeeCalc()
        self.assertRaises(ValueError, calc.calculate, arg1)

    def test_more_than_20000_value(self):
        """ Testing whether value errors raised when more than 20000 loan value is given. """
        arg1 = LoanData(loan=400000, term=Term.TERM_12)
        calc = FeeCalc()
        self.assertRaises(ValueError, calc.calculate, arg1)

    def test_string_value(self):
        """ Testing whether type errors raised when string value is given. """
        arg1 = LoanData(loan="ASD", term=Term.TERM_12)
        calc = FeeCalc()
        self.assertRaises(TypeError, calc.calculate, arg1)

    def test_boolean_value(self):
        """ Testing whether type errors raised when boolean value is given. """
        arg1 = LoanData(loan=True, term=Term.TERM_12)
        calc = FeeCalc()
        self.assertRaises(TypeError, calc.calculate, arg1)

    def test_complex_value(self):
        """ Testing whether type errors raised when complex value is given. """
        arg1 = LoanData(loan=5 + 6j, term=Term.TERM_12)
        calc = FeeCalc()
        self.assertRaises(TypeError, calc.calculate, arg1)

    def test_proper_integer_value(self):
        """ Testing whether equals of the right value when edge parameter is given. """
        arg1 = LoanData(loan=1000, term=Term.TERM_24)
        calc = FeeCalc()
        self.assertEqual(calc.calculate(arg1), 70)

    def test_proper_float_value(self):
        """ Testing whether rounded value to multiple of 5 returned when none integer value is given. """
        arg1 = LoanData(loan=1005.55, term=Term.TERM_24)
        calc = FeeCalc()
        self.assertEqual(calc.calculate(arg1), 75)

    def test_incorrect_term_value(self):
        """ Testing whether value errors raised when wrong term is given. """
        arg1 = LoanData(loan=1005.55, term=6)
        calc = FeeCalc()
        self.assertRaises(ValueError, calc.calculate, arg1)
