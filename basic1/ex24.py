"""
Write a Python program to test whether a passed letter is a vowel or not. 

"""
#My code
import re

def isVowel(letter):
    if re.search("[aeiou]",letter) == None:
        print("Not a vowel")
    else:
        print("Is vowel")

isVowel("a")
isVowel("k")

#Sample code
"""
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))
"""