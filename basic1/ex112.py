"""
    Write a Python program to remove the first item from a specified list.
"""
#My code
def rmList(aList):
    aList.pop(0)
    return aList

print(rmList([2,3,6]))

#Sample code
"""
color = ["Red", "Black", "Green", "White", "Orange"]
print("\nOriginal Color: ",color)
del color[0]
print("After removing the first color: ",color)
print()
"""