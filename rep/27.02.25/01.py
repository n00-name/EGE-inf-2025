import re

n = 240
s = open('24-295.txt').readline()
t = re.sub('DE', 'D E', s).split()
print(t)
print(max([len("".join(t[x:x + n + 1])) for x in range(len(t) - n - 1)]))