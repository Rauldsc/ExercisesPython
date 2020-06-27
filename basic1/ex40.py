"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""
import math
def distance(point1,point2):
    d = [point2[0] - point1[0], point2[1] - point1[1]]
    return math.sqrt(d[0]**2+d[1]**2)

print(distance([1,2],[2,3]))