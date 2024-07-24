ans = 0

for n1 in range(1, 5):
    for n2 in range(0, 5):
        for n3 in range(0, 5):

            if n1 >= n2 and n2 >= n3:
                ans += 1
print(ans) # 34
