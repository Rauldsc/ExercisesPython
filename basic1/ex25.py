"""
Write a Python program to check whether a 
specified value is contained in a group of values.

"""
import re
def isInGroup(aList,aValue):
    if aValue in aList:
        return("Is contained")
    else:
        return("Is not contained")

print(isInGroup(["a","b","c"],"j"))
print(isInGroup(["a","b","c"],"a"))