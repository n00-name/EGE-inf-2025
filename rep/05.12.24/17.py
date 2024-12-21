import math

# Открываем файл и считываем данные
with open('17-411.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Инициализируем переменные для подсчета пар и минимальной суммы
count = 0
min_sum = float('inf')

# Перебираем элементы и проверяем условия
for i in range(len(nums) - 1):
    a = nums[i]
    b = nums[i + 1]

    # Проверяем, что числа имеют разную четность
    if (a % 2 != b % 2):
        # Проверяем, что числа взаимно просты
        if math.gcd(a, b) == 1:
            count += 1
            # Обновляем минимальную сумму
            pair_sum = a + b
            if pair_sum < min_sum:
                min_sum = pair_sum

# Выводим результат
print(count, min_sum)
