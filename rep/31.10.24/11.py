# Solution for task 58
with open("k8-25.txt", "r") as F:
    s = F.readline()

maxLen, curLen = 1, 1
maxChar = s[0]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        curLen += 1
        if curLen > maxLen:
            maxLen = curLen
            maxChar = s[i]
    else:
        curLen = 1

print(maxChar, maxLen)
