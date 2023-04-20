'''
Instructions:
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
'''
import unittest
from random import randint

def alphabet_position(text):
    #Create a Dictionary for alphabet and its positions
    alpha_dic = {
        "a" : "1",
        "b" : "2",
        "c" : "3",
        "d" : "4",
        "e" : "5",
        "f" : "6",
        "g" : "7",
        "h" : "8",
        "i" : "9",
        "j" : "10",
        "k" : "11",
        "l" : "12",
        "m" : "13",
        "n" : "14",
        "o" : "15",
        "p" : "16",
        "q" : "17",
        "r" : "18",
        "s" : "19",
        "t" : "20",
        "u" : "21",
        "v" : "22",
        "w" : "23",
        "x" : "24",
        "y" : "25",
        "z" : "26",
    }
    
    #create a stack to store each postion
    result = []
    #Make all characters lower case and check if present in alpha_dic and store value(position) in stack
    for i in text.lower():
        if i in alpha_dic:
            result.append(alpha_dic[i])
    
    #join items in stack into 1 string and return
    return " ".join(result)
        
class TestValidBrace(unittest.TestCase):
    def test_basic_words(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

    def test_basic_numbers(self):
        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(alphabet_position(number_test), "")

if __name__ == "__main__":
    unittest.main()