"""
Write a Python program to sum of three given integers.
 However, if two values are equal sum will be zero.

"""

def threeNumbers (n1,n2,n3):
    if n1 == n2 or n2 == n3 or n1 == n3:
        return 0
    else:
        return n1+n2+n3

print(threeNumbers(4,12,6))
print(threeNumbers(6,12,6))