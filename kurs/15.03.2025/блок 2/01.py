count = 0
nm = -1

for i in range(1512, 13203):
    if i % 7 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
        count += 1
        nm = max(nm, i)
print(count, nm)