"""
    Write a Python function that takes a positive integer and returns
     the sum of the cube of all the positive integers smaller than the specified number.
"""
#My code
def sumofcube(num):
    sum = 0
    for i in range(0,num):
        sum += i**3
    return sum

print(sumofcube(5))

#Sample code
"""
def sum_of_cubes(n):
  n -= 1
  total = 0
  while n > 0:
    total += n * n * n
    n -= 1
  return total
print("Sum of cubes: ",sum_of_cubes(3))
"""