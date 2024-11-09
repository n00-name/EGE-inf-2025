with open("k7a-3.txt", "r") as F:
    s = F.read()

count = 0
maxCount = 0

for char in s:
    if char in 'ABEF':
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 0

print(maxCount)
