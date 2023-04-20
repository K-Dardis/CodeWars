'''
Instructions:
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python
'''
import unittest

def valid_braces(string):
    #Create a braces pairing using dictionary
    braces= {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }
    
    #Create an Array to act as a stack
    brace_check = []
    
    for b in string:
        #check if the element is one of the keys in braces dictionary and add its value to the braces_check stack
        if b in braces:
            brace_check.append(braces[b])
        else:
            #Check if there is any elements in braces_check stack
            if brace_check:
                #Compare element to last item in stack
                if b != brace_check.pop():
                    return False
                continue
            return False
    
    #Check that no Items remain in stack 
    return True if not brace_check else False
        
class TestValidBrace(unittest.TestCase):
    def test_basic(self):
        def check_valid(string):
            self.assertEqual(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))
    
        def check_invalid(string):
            self.assertEqual(valid_braces(string), False, 'Expected "{0}" to be valid'.format(string))

        check_valid( "()" )
        check_invalid( "(}" )
        check_valid( "[]" )
        check_invalid("[(])")
        check_valid( "{}" )
        check_valid( "{}()[]" )
        check_valid( "([{}])" )
        check_invalid( "([}{])" )
        check_valid( "{}({})[]" )
        check_valid( "(({{[[]]}}))" )
        check_invalid( "(((({{" )
        check_invalid( ")(}{][" )
        check_invalid( "())({}}{()][][" )

if __name__ == "__main__":
    unittest.main()