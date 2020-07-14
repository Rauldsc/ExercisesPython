"""
    Write a Python program to create the combinations of 3 digit combo.
"""

import random, math

def combo(d1,d2,d3):
    combos = []
    digits = list((str(d1),str(d2),str(d3)))
    while(len(combos) < math.factorial(len(digits))):

        random.shuffle(digits)
        if ''.join(digits) not in combos:
            combos.append(''.join(digits))
    print(combos)

combo(1,5,6)