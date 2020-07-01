"""
Write a Python program to concatenate N strings.
"""
"""
#My code
def concatenate(Nstring):
    str1 = ""
    for i in Nstring:
        str1 += i
    return str1

print(concatenate(["Hello"," World"]))
"""
#Sample code
def concatenate(Nstring):
    str1 = "".join(Nstring)
    return str1

print(concatenate(["Hello"," World"]))