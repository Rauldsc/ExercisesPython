"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

#My code
import math

def gcd(num1, num2):
    return(math.gcd(num1,num2))

print(gcd(4,6))

#Sample code
"""
def gcd(num1,num2):
    gcd = 1
    if num1 % num2 == 0:
        return num1
    
    for k in range(int(num1 / 2), 0, -1):
        if num1 % k == 0 and num2 % k == 0:
            gcd = k
            break  
    return gcd

print(gcd(12, 1160))
print(gcd(4, 6))
"""