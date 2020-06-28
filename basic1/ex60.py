"""
Write a Python program to calculate the hypotenuse of a right angled triangle.
"""
import math
def hypotenuse(leg1,leg2):
    return math.sqrt(leg1**2 + leg2**2)

print(hypotenuse(3,4))