with open('17_03_401.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Найдем максимальный элемент, оканчивающийся на 7
max_ending_with_7 = max(x for x in nums if x % 10 == 7)

# Переменные для хранения результата
count = 0
unique_elements = set()  # Множество для уникальных чисел

# Перебор троек
for i in range(len(nums) - 2):
    triple = nums[i:i + 3]
    odd_count = sum(1 for x in triple if x % 2 != 0)
    greater_count = sum(1 for x in triple if x > max_ending_with_7)

    # Проверяем условия
    if odd_count == 2 and greater_count == 1:
        count += 1
        unique_elements.update(triple)

# Вычисление среднего арифметического
if unique_elements:
    avg = sum(unique_elements) / len(unique_elements)
    result_digits = str(int(avg))[:3]  # Три старших разряда
else:
    result_digits = "000"

print(count, result_digits)
