"""
Write a Python program to convert pressure in kilopascals to pounds per square inch,
 a millimeter of mercury (mmHg) and atmosphere pressure.
"""

def pressure(kpa):
    psi = kpa / 6.895
    mmhg = kpa*760/101.325
    atm = kpa/101.325
    return[psi,mmhg,atm]

print(pressure(12))
