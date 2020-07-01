"""
    Write a Python program to compute the product of a list of integers (without using for loop).
"""

from functools import reduce

def product(nums):
    nums_product = reduce( (lambda x, y: x * y), nums)
    return nums_product

print(product([2,7,5,12]))