"""
    Write a Python function to check whether a number is 
    divisible by another number. Accept two integers values form the user
"""

def multiple(x, y):
	return True if x % y == 0 else False

print(multiple(5,3))