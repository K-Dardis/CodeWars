'''
Instructions:
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
    123  --> "123"
    999  --> "999"
    -100 --> "-100"

https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
'''

import unittest

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

class TestNumberToString(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(number_to_string(67), '67')
        self.assertEqual(number_to_string(79585), '79585')
        self.assertEqual(number_to_string(79585), "79585")
        self.assertEqual(number_to_string(1+2), '3')
        self.assertEqual(number_to_string(1-2), '-1')
   
if __name__ == "__main__":
    unittest.main()