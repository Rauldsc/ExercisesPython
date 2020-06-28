"""
Write a Python program to convert seconds to day, hour, minutes and seconds
"""

def time(seconds):
    d = seconds // (24*3600)
    seconds %=  (24*3600)
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    seconds %= 60
    print("{}:{}:{}:{}".format(d,h,m,seconds))

time(1234565)