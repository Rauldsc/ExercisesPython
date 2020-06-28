"""
Write a Python program to convert all units of time into seconds.
"""

def seconds(d,h,m,s):
    return 3600*24*d + 3600*h + 60*m +s

print(seconds(4,5,20,10))