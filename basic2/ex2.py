"""
    Write a Python program to create all
    possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
"""
import math
import random
vowels = ['a','e','i','o','u']
combinations = []

while len(combinations) <  math.factorial(5):
    random.shuffle(vowels)
    if "".join(vowels) not in combinations:
        combinations.append("".join(vowels))
        
print(combinations)
