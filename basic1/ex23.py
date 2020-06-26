"""
Write a Python program to get the n (non-negative integer) copies of the 
first 2 characters of a given string. Return the n copies of the whole string 
if the length is less than 2.

"""
def stringCopies(aString, copies):
    
    
    if len(aString) < 2:

        if(int(copies) >= 0):
            return(copies*aString)
        else:
            return("No valide number")
    else:
        newString = aString[0]+aString[1]
        if(int(copies) >= 0):
            return(copies*newString)
        else:
            return("No valide number")

print(stringCopies("1",2))
print(stringCopies("Hello World",3))