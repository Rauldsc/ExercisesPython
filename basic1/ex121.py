"""
    Write a Python program to determine whether variable is defined or not. 
"""

try: x = 2
except NameError: print("Variable is not defined")
else: print("Variable is defined")