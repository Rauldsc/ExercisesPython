"""
Write a Python program to count the number 4 in a given list.

"""

def searchFour(aList):
    count = 0
    for i in aList:
        if i == 4:
            count = count + 1
    return(count)

print(searchFour([1,2,4,8,4]))