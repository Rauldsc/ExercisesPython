"""
 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

"""
#My solution

try:
    n = int(input("Sample value: "))
    print("{}".format(n+n*n+n*n*n))


except:
    print("Next time put a number")


#Sample solution
"""
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""