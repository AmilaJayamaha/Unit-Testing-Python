import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # Test addition
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)

    # Test subtraction
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(0, 0), 0)

    # Test multiplication
    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(0, 10), 0)

    # Test division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)

    # Test division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    # Test invalid input
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            subtract(5, "3")
        with self.assertRaises(TypeError):
            multiply("2", 4)
        with self.assertRaises(TypeError):
            divide(10, "2")

if __name__ == "__main__":
    unittest.main()
