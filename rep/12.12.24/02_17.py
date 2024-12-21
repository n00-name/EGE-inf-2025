# Функция для вычисления НОД без использования math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Чтение чисел из файла
with open('17-411-2.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Словарь для хранения частоты вхождения НОД и максимальной суммы для каждого НОД
gcd_counter = {}
max_sum_for_gcd = {}

# Перебор всех пар подряд
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    gcd_value = gcd(a, b)  # Вычисляем НОД для пары

    # Увеличиваем счетчик для этого НОД
    if gcd_value not in gcd_counter:
        gcd_counter[gcd_value] = 1
    else:
        gcd_counter[gcd_value] += 1

    # Обновляем максимальную сумму для данного НОД
    pair_sum = a + b
    if gcd_value not in max_sum_for_gcd or pair_sum > max_sum_for_gcd[gcd_value]:
        max_sum_for_gcd[gcd_value] = pair_sum

# Находим наиболее часто встречающийся НОД
most_common_gcd = max(gcd_counter, key=gcd_counter.get)

# Ответ: наиболее частый НОД и максимальная сумма для этого НОД
print(most_common_gcd, max_sum_for_gcd[most_common_gcd])
