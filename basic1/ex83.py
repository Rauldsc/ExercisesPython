"""
Write a Python program to test whether all numbers of a list is greater than a certain number.
"""

def greater(aList, n):
    return max(aList) > n

print(greater([9,6,5],2))
print(greater([9,6,5],10))