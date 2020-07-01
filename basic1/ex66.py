"""
Write a Python program to calculate body mass index.
"""


def imc(weight,height):
    return weight/height**2

print(imc(80,1.78))