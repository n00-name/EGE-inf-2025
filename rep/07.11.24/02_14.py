xmax = 0
max_equal_count = -1

for x in range(1, 10001):
    y = 6 ** 900 + 6 ** 10 - x
    count_3 = 0
    count_5 = 0

    # Convert y to base 6 and count occurrences of '3' and '5'
    while y != 0:
        digit = y % 6
        if digit == 3:
            count_3 += 1
        elif digit == 5:
            count_5 += 1
        y //= 6

    # Check if the count of '3's equals the count of '5's
    if count_3 == count_5:
        max_equal_count = max(max_equal_count, count_3)
        if count_3 == max_equal_count:
            xmax = max(xmax, x)

print(xmax)
