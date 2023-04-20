'''
instructions:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
'''

import unittest

def generate_hashtag(s):
    hash_word = s.title().strip().replace(" ", "")
    
    if not hash_word:
        return False
    elif len(hash_word) > 140 - 1:
        return False
    else:
        return f'#{hash_word}'
    
class TestHashtagGenerator(unittest.TestCase):
    def test_basic_correct(self):
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEqual(generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
        self.assertEqual(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
        self.assertEqual(generate_hashtag('c i n'), '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        
    def test_basic_incorrect(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEqual(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final string is longer than 140 chars.')

if __name__ == "__main__":
    unittest.main()