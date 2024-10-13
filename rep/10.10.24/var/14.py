x = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011

s = []
while x != 0:
    s.append(x % 31)
    x //= 31
s.reverse()

print(s)

sum = 0
for num in s:
    if num <= 17:
        sum += num
print(sum)