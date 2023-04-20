'''
Instructions:
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.

https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
'''
import unittest

def solution(n):
    # Create a Dictionary pairing digits with roman numerals.
    # Had to add extra as certian repetitions could occur with certian numerals.
    roman_dic = {
        1 : "I",
        4 : "IV", #extra
        5 : "V",
        9 : "IX", #extra
        10 : "X",
        40 : "XL", #extra
        50 : "L",
        90 : "XC", #extra
        100 : "C",
        400 : "CD", #extra
        500 : "D",
        900 : "CM", #extra
        1000 : "M",
    }
    number = n
    numeral = ""
    
    #we then sort the dictionary in descending order of keys, incase they are not in order or changed
    for i in sorted(roman_dic.keys(), reverse=True):
        #as long as the number is greater than 0 we can add more numerals
        if number > 0:
            #calculate how many times the key can go into the number and use that as the multiple against the key value.
            numeral += roman_dic[i] * (number // i) 
            #reduce the number to the remainding amount when the the total of keys value is taken out
            number %= i
    
    return numeral
        
class TestValidBrace(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(solution(1),'I', "solution(1),'I'")
        self.assertEqual(solution(4),'IV', "solution(4),'IV'")
        self.assertEqual(solution(6),'VI', "solution(6),'VI'")
        self.assertEqual(solution(14),'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21),'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91),'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")

if __name__ == "__main__":
    unittest.main()