"""
    Write a Python program to get system command output.
"""

import subprocess
# file and directory listing
returned_text1 = subprocess.check_output("dir", shell=True, universal_newlines=True)
returned_text2 = subprocess.check_output("cat ex61.py", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text1)
print("content of file")
print(returned_text2)