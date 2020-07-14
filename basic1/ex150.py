"""
    Write a Python function to find a distinct
    pair of numbers whose product is odd from a sequence of integer values
"""

#My code
def oddseq(l):
    count = 0
    for i in l:
        if i % 2 == 0: pass
        else: count += 1
    return count < 2

print(oddseq([2,3,1]))

#Sample code
"""
def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
          return False
          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
"""