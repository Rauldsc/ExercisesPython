"""
Write a Python program to find whether a given number (accept from the user)
 is even or odd, print out an appropriate message to the user.

"""


try:
    number = int(input("Input a number: "))

    if (number % 2) == 0:
        print("The number is even")
    else:
        print("The number is odd")
except:
    print("Please, input a valid value")