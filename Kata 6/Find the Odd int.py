'''
Instructions:
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
'''
import unittest

def find_it(seq):
    for i in seq:
        total = seq.count(i)
        if total % 2 != 0:
            return i
        
class TestFindOddint(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([10, 10, 10]), 10)
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)

if __name__ == "__main__":
    unittest.main()