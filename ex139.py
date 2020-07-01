"""
    Write a Python program to valid a IP address.
"""

import socket
addr = '127.0.0.1'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")