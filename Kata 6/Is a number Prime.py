'''
Instructions:
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */

https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
'''
import unittest
import math

def is_prime(num):
    if num > 1: 
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i) == 0:
                return False
        return True
    return False
        
class TestValidBrace(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_prime(0),  False, "0  is not prime")
        self.assertEqual(is_prime(1),  False, "1  is not prime")
        self.assertEqual(is_prime(2),  True, "2  is prime")
        self.assertEqual(is_prime(73), True, "73 is prime")
        self.assertEqual(is_prime(75), False, "75 is not prime")
        self.assertEqual(is_prime(-1), False, "-1 is not prime")

    def test_prime(self):
        self.assertEqual(is_prime(3),  True, "3  is prime")
        self.assertEqual(is_prime(5),  True, "5  is prime")
        self.assertEqual(is_prime(7),  True, "7  is prime")
        self.assertEqual(is_prime(41), True, "41 is prime")
        self.assertEqual(is_prime(5099), True, "5099 is prime")

    def test_not_prime(self):
        self.assertEqual(is_prime(4),  False, "4  is not prime")
        self.assertEqual(is_prime(6),  False, "6  is not prime")
        self.assertEqual(is_prime(8),  False, "8  is not prime")
        self.assertEqual(is_prime(9), False, "9 is not prime")
        self.assertEqual(is_prime(45), False, "45 is not prime")
        self.assertEqual(is_prime(-5), False, "-5 is not prime")
        self.assertEqual(is_prime(-8), False, "-8 is not prime")
        self.assertEqual(is_prime(-41), False, "-41 is not prime")


if __name__ == "__main__":
    unittest.main()