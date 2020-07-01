"""
Write a Python program to sort three integers without using conditional statements and loops
"""

#My code
def sortN(n1,n2,n3):
    n = sorted([n1,n2,n3])
    print(n)
    return print("{},{},{}".format(*n))

sortN(12,5,1)

#Sample code

"""
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
"""