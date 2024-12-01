from fnmatch import fnmatch

for x in range(10**9, 10**10, 2023):
    if fnmatch(str(x), '1*1'):
        digit_sum = sum(map(int, str(x)))  # Сумма цифр числа
        print(x, x // 2023, digit_sum)