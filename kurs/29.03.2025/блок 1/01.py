from fnmatch import fnmatch
num = 103456709
del_ = 17
start = num - num % del_

for i in range(start, 10**10, del_):
    if fnmatch(str(i), '1?34567?9'):
        print(i,i//del_)