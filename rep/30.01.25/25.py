from fnmatch import *

divisor = 31007
mask = "1*34?5?9"

for x in range(0, 10**10, divisor):
    if fnmatch(str(x), mask):
        print(x, x // divisor)