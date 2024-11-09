with open("k7b-5.txt", "r") as F:
    s = F.read()

count = 0
maxCount = 0

for char in s:
    if (char == 'C' and count % 2 == 0) or \
       (char == 'A' and count % 2 == 1):
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1 if char == 'C' else 0

print(maxCount)
