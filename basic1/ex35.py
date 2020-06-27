"""
Write a Python program that will return true if the two
 given integer values are equal or their sum or difference is 5.
"""

def mathStuff(n1,n2):
    sum = n1+n2
    diff = n1-n2
    if n1 == n2 or sum == 5 or abs(diff) == 5:
        return True
    else:
        return False

print(mathStuff(9,2))
print(mathStuff(3,2))  