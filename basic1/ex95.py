"""
Write a Python program to check whether a string is numeric.
"""

def isNumeric(s):
    try:
        int(s)
        print("The string is numeric")
    except:
        print("The string is not numeric")

isNumeric("278")
isNumeric("545sd")