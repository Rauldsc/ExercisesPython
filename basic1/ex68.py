"""
Write a Python program to calculate the sum of the digits in an integer.
"""

def digits(num):
    n = str(num)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

print(digits(18145))