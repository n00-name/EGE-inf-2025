# Solution for task 76
with open("k8-18.txt", "r") as F:
    s = F.readline()

maxLen, curLen = 1, 1
c = [s[0]]  # List to store characters of longest substrings

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        curLen += 1
        if curLen == maxLen:
            c.append(s[i])  # Add character to list if it matches current max length
        elif curLen > maxLen:
            maxLen = curLen
            c = [s[i]]  # Reset list with new character for the longest length
    else:
        curLen = 1

for c1 in c:
    print(c1, maxLen)
