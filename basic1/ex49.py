"""
Write a Python program to list all files in a directory in Python.
"""

from os import listdir
from os.path import isfile, join
path = "/home/raul/Escritorio/exercisesPython/basic1"
files_list = [f for f in listdir(path) if isfile(join(path, f))]
print(files_list)