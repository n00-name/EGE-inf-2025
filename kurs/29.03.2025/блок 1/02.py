from fnmatch import fnmatch
num = 1235670
del_ = 169
start = num - num % del_

for i in range(start, 10**9, del_):
    if fnmatch(str(i), '123*567?'):
        print(i,i//del_)