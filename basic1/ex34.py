"""
Write a Python program to sum of two given integers.
 However, if the sum is between 15 to 20 it will return 20
"""

#My code
def sum(n1,n2):
    s = n1+n2
    if s > 15 and s < 20: #s in range(15, 20)
        return 20
    else:
        return s

print(sum(12,12))
print(sum(4,12))

