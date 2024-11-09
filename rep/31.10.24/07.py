with open("k7c-4.txt", "r") as F:
    s = F.read()

count = 0

for i in range(len(s) - 2):
    if s[i+2] in 'CDF' and s[i] in 'ADF' and s[i+1] in 'ADF' and s[i] != s[i+2] and s[i+1] != s[i+2]:
        count += 1

print(count)
