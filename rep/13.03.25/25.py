from fnmatch import *

divisor = 2025
mask1 = '33?2*42?'
mask2 = '*32??2?'

for x in range(0, 10**10, divisor):
    if fnmatch(str(x), mask1) and fnmatch(str(x), mask2):
        print(x, x // divisor)