with open("k7b-6.txt", "r") as F:
    s = F.read()

count = 0
maxCount = 0

for char in s:
    if (char == 'D' and count % 3 == 0) or \
       (char == 'A' and count % 3 == 1) or \
       (char == 'F' and count % 3 == 2):
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1 if char == 'D' else 0

print(maxCount)
