"""
 Write a Python program to create a histogram from a given list of integers.

"""
#My code

def histogram(aList):
    for i in aList:
        print("{}".format("*"*i))

histogram([2,3,5])

#Sample code
"""
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])
"""