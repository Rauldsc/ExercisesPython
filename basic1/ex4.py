"""
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504

"""

#My solution
"""
import math, sys
arg = sys.argv
radius = arg[1]

print(math.pi*pow(int(radius),2))
"""
#Sample solution

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))