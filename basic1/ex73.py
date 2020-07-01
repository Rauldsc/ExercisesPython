"""
Write a Python program to calculate midpoints of a line.
"""

def midpoint(p1,p2):
    return [(p2[0] + p1[0])/2,(p2[1]+p1[1])/2]

print(midpoint([3,2],[4,5]))