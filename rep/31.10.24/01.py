with open("k7-44.txt", "r") as F:
    s = F.readline()
    maxLen, cLen = 0, 0
    for c in s:
        if c == 'C':
            cLen += 1
            if cLen > maxLen:
                maxLen = cLen
        else:
            cLen = 0
    print(maxLen)
