"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

def stringCopies(aString, copies):
    
    if(int(copies) >= 0):
        return(copies*aString)
    else:
        return("No valide number")

print(stringCopies("Hello World",-2))
print(stringCopies("Hello World",3))

