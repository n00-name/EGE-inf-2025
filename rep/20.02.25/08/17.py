# Чтение данных из файла
with open('17var08.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))  # Преобразуем в список целых чисел

# Находим минимальный элемент, который заканчивается на 700
min_ending_700 = float('inf')
for num in nums:
    if num % 1000 == 700:  # Проверяем, заканчивается ли число на 700
        min_ending_700 = min(min_ending_700, num)

# Проверка для каждой тройки
valid_trios = []
for i in range(len(nums) - 2):
    trio = nums[i:i + 3]  # Тройка подряд идущих элементов
    five_digit_count = sum(10000 <= abs(x) <= 99999 for x in trio)  # Количество пятизначных чисел

    if five_digit_count <= 2:  # Условие, что не более двух чисел пятизначные
        trio_sum = sum(trio)
        if trio_sum >= min_ending_700:  # Условие на сумму
            valid_trios.append(trio_sum)

# Результаты
if valid_trios:
    print(len(valid_trios), min(valid_trios))  # Количество троек и минимальная сумма
else:
    print(0, 0)  # Если нет таких троек
