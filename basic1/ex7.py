"""
Write a Python program to accept a filename from the user and print the extension of that.

"""

filename = input("Input your filename with extension: ")
filenameList = filename.split(".")
print("The extension is: " + filenameList[-1])
