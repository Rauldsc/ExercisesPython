"""
 Write a Python program to get the difference between a given number and 17,
  if the number is greater than 17 return double the absolute difference.

"""


def difference(number):
    if number <= 17:
        print(17-number)
    else:
        print(2*abs(17-number))
        #Sample code: print(2*(number-17))
difference(9)
difference(30)


