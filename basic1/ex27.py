"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""

def concatenate(aList):
    holder = ""
    for i in aList:
        holder += str(i)
    return(holder)

print(concatenate([23,"Hello", " Peter"]))
        