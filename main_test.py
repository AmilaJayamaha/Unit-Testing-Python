# main_test.py
import unittest
import Calculator_steps as CalculatorClass

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorClass.Calculator()  # Instantiate the Calculator Class
    
    def tearDown(self):
        self.calculator = None  # Clean up after each test
    
    def test_DecimalValues(self):
        # Verify Calculator accepts only whole numbers
        result = self.calculator.add(2.5, 3)
        self.assertIsNone(result)  # The result should be None
    
    def test_NonNumeric(self):
        # Verify Calculator does not accept non-numeric values
        result = self.calculator.add("abc", 5)
        self.assertIsNone(result)  # The result should be None
    
    def test_MoreThanThreeIntegers(self):
        # Verify Calculator does not accept more than 3 numbers
        result = self.calculator.add(2, 3, 4, 5)
        self.assertIsNone(result)  # The result should be None
    
    def test_MoreThan100(self):
        # Verify Calculator does not accept numbers greater than 100
        result = self.calculator.add(101, 50)
        self.assertIsNone(result)  # The result should be None

if __name__ == '__main__':
    unittest.main()
