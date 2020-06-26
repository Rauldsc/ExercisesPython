"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

"""

a = input("Input numbers comma-separated: ")

numbersList = a.split(",")
numbersTuple = tuple(numbersList)
print(numbersList)
print(numbersTuple)