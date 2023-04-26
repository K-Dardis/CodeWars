'''
instructions:
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
'''

import unittest

def rgb(r, g, b):
    #method to check if the given value are in range if not return closest value
    def range_correction(num):
        if 0 > num or num > 255:
            return min((0, 255), key=lambda x:abs(x-num))
        return num
    return(('{:02x}{:02x}{:02x}'.format(range_correction(r), range_correction(g), range_correction(b))).upper())

class TestRGBToHex(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
        
if __name__ == "__main__":
    unittest.main()

