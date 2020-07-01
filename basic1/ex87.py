"""
Write a Python program to get the size of a file.
"""

import os
def sizeofFile(file):
    return os.path.getsize(file)

print(sizeofFile("ex20.py"))


