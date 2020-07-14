"""
     Write a Python function that takes a sequence of numbers
    and determines whether all the numbers are different from each othe
"""

def repeated(l):
    return len(l) != len(set(l))

print(repeated([2,3,15]))
