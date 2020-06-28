"""
Write a Python program to convert height (in feet and inches) to centimeters.
"""
#My Code

def feetCm(ft):
    return ft*30.48

def inchesCm(inch):
    return inch*2.54

print(feetCm(4))
print(inchesCm(4))

#Sample Code
"""
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)
"""