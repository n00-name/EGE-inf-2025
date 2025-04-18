with open("17-2.txt") as f:
    nums = list(map(int, f.readlines()))

# Находим минимальный элемент
min_value = min(nums)

# Подсчитываем количество его вхождений
count = nums.count(min_value)

# Находим индекс последнего вхождения (нумерация с 1)
last_position = len(nums) - nums[::-1].index(min_value)

print(count, last_position)
