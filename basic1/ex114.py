"""
     Write a Python program to filter the positive numbers from a list.
"""

def filt(aList):
    new_list = list(filter(lambda x: x >0, aList))
    return new_list

print(filt([8,-4,2,-5]))
