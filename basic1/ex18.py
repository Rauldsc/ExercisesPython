"""
Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum.

"""

def threeNumbers(n1,n2,n3):
    if n1 == n2 == n3:
        return(9*n1)
    else:
        return (n1+n2+n3)

print(threeNumbers(8,12,35))
print(threeNumbers(2,2,2))