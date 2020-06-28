"""
Write a python program to find the sum of the first n positive integers.
"""
#My code
def summatory(n):
    x = 0
    for i in range(0,n+1):
        x += i
    return x

print(summatory(8))  

#Sample code
"""
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print(sum_num)
"""
       
    