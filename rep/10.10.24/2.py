import math

with open('17-2.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

min_elem = min(nums)

min_last_digit = min_elem % 10

count = 0
max_sum = float('-inf')


for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]

    # Вычисляем НОД пары
    gcd_ab = math.gcd(a, b)

    # Последняя цифра НОД
    gcd_last_digit = gcd_ab % 10

    # Проверяем условие задачи
    if gcd_last_digit == min_last_digit:
        count += 1
        pair_sum = a + b

        if pair_sum > max_sum:
            max_sum = pair_sum

print(count, max_sum)
