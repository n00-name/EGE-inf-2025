# Функция для проверки, записывается ли число в системе счисления с заданным количеством разрядов
def check_in_base(num, base, digits):
    representation = []
    while num > 0:
        representation.append(num % base)
        num //= base
    return len(representation) == digits

# Читаем данные из файла
with open("17-418.txt") as f:
    data = list(map(int, f.readlines()))

# Находим минимальный элемент, который записывается в шестеричной системе как четырёхзначное число
min_element_base6 = min(x for x in data if check_in_base(x, 6, 4))

# Находим минимальный элемент, который записывается в девятеричной системе как трёхзначное число
min_element_base9 = min(x for x in data if check_in_base(x, 9, 3))

# Остатки для проверки условий
remainder_5 = min_element_base6 % 5
remainder_13 = min_element_base9 % 13

count = 0
min_sum = float('inf')

# Перебор троек
for i in range(len(data) - 2):
    triplet = data[i:i + 3]

    # Условие для остатка от деления на 11
    remainder_11_check = sum(1 for x in triplet if x % 11 == remainder_5) == 1

    # Условие для остатка от деления на 7
    remainder_7_check = sum(1 for x in triplet if x % 7 == remainder_13) == 1

    if remainder_11_check and remainder_7_check:
        count += 1
        min_sum = min(min_sum, sum(triplet))

print(count, min_sum)
