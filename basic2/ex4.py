"""
    Write a Python program to find unique triplets
     whose three elements gives the sum of zero from an array of n integers.
"""

def triplets(l):
    combos = []
    l.sort()
    for i in range(len(l) - 2):
        for j in range(1 , len(l)-1):
            for k in range(2 , len(l)):
                result = l[i] + l[j] + l[k]
                if result == 0:
                    num = list((l[i],l[j],l[k]))
                    num = sorted(num)
                    if num not in combos:
                        combos.append(num)
    return combos

print(triplets([-2,3,4,1,-1,0,-4]))


        
        
