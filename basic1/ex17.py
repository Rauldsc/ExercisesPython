"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.

"""

#My code

def checker(number):
    if (number >= 900) and (number <= 1100) or (number >= 1900) and (number <= 2100):
        print("Yeep!")
    else:
        print("Nahh..")

checker(2200)
checker(1053)

#Sample code
"""
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
"""