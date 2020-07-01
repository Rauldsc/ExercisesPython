"""
    Write a Python function to find the maximum and minimum numbers from a sequence of numbers
    Note: Do not use built-in functions.
"""

def maxmin(l):
    maximum = l[0]
    minimum = l[0]
    for i in l:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return maximum,minimum

print(maxmin([23,4,3,24,-5]))
