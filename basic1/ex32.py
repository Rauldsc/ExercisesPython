"""
Write a Python program to get the least common multiple (LCM) of two positive integers.
"""

def lcm(n1,n2):

   if n1 > n2:
       n3 = n1
   else:
       n3 = n2

   while(True):
       if((n3 % n1 == 0) and (n3 % n2 == 0)):
           lcm = n3
           break
       n3 += 1

   return lcm

print(lcm(8,5))
