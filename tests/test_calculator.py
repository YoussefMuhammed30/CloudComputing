import unittest
from calculator.calculator import Calculator


class TestCalculatorAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_add_mixed_sign(self):
        self.assertEqual(self.calc.add(-3, 5), 2)

    def test_add_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(1.1, 2.2), 3.3, places=5)


class TestCalculatorSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_resulting_negative(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtract_same_numbers(self):
        self.assertEqual(self.calc.subtract(7, 7), 0)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=5)


class TestCalculatorMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_two_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=5)


class TestCalculatorDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide_even(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_resulting_float(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)


class TestCalculatorPower(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_power_positive(self):
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_power_zero_exponent(self):
        self.assertEqual(self.calc.power(99, 0), 1)

    def test_power_one_exponent(self):
        self.assertEqual(self.calc.power(7, 1), 7)

    def test_power_negative_base(self):
        self.assertEqual(self.calc.power(-2, 3), -8)


class TestCalculatorModulo(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

    def test_modulo_by_zero_raises(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)


if __name__ == "__main__":
    unittest.main()
