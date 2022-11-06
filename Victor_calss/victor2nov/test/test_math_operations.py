import unittest
#import math_operations
from math_operations import add, subtraction, division, multiplication

class TestOperation(unittest.TestCase):
    
    def test_operations(self):
        self.assertEqual(add(2, 2), 4)
        # result = add(2, 2)
        # expected_result = 4
        # self.assertEqual(result,expected_result)  #another way
        self.assertEqual(subtraction(2, 2), 0)
        self.assertEqual(division(2, 2), 1)
        self.assertEqual(multiplication(2, 2), 4)        


if __name__=='__main__':
    unittest.main()


