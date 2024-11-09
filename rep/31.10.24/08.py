with open("k7b-4.txt", "r") as F:
    s = F.readline()

count = 0
maxCount = 0

for char in s:
    if (char == 'E' and count % 4 == 0) or \
       (char == 'B' and count % 4 == 1) or \
       (char == 'C' and count % 4 == 2) or \
       (char == 'F' and count % 4 == 3):
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 1 if char == 'E' else 0

print(maxCount)
