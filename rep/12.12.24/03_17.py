# Чтение чисел из файла
with open('17-411-3.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Находим минимальный элемент, кратный 3
min_multiple_of_3 = min(num for num in nums if num % 3 == 0)

# Находим максимальный элемент, заканчивающийся на 3
max_ending_with_3 = max(num for num in nums if num % 10 == 3)

# Счетчики для количества пар и минимальной суммы квадратов
count = 0
min_sum_of_squares = float('inf')

# Перебор всех пар подряд
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]

    # Проверяем, что ровно одно из чисел соответствует условию
    condition_a = min_multiple_of_3 <= a <= max_ending_with_3
    condition_b = min_multiple_of_3 <= b <= max_ending_with_3

    if condition_a != condition_b:  # Только одно из чисел должно удовлетворять условию
        count += 1
        sum_of_squares = a ** 2 + b ** 2
        min_sum_of_squares = min(min_sum_of_squares, sum_of_squares)

# Выводим результат
print(count, min_sum_of_squares)
