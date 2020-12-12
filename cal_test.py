import cal_code
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = cal_code.add(3, 5)
        self.assertEqual(result, 8)
        
    def test_subtraction(self):
        result = cal_code.subtract(5, 2)
        self.assertEqual(result, 3)
        
        
if __name__ == '__main__':
    unittest.main()
