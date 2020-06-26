"""
Write a Python program to get a new string from a given string where 
"Is" has been added to the front. If the given string already begins with "Is" 
then return the string unchanged.

"""
#My code

def addIs(aString):
    if(aString[0] == "I" and aString[1] == "s"):
        return(aString)
    else:
        return("Is" + aString)

print(addIs("Peter"))
print(addIs("Is Kevin"))

#Sample code

"""
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
"""