"""
    Write a Python program to input a number, if it is not a number generate an error message
"""

try:

    int(input("Input a number: "))

except ValueError:
    print("\nNaN")
