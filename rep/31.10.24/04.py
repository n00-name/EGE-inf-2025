with open("k8-3.txt", "r") as F:
    s = F.readline()
    maxLen, curLen = 1, 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            curLen += 1
            if curLen > maxLen:
                maxLen = curLen
        else:
            curLen = 1
    print(maxLen)
