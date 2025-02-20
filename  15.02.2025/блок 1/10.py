# Функция для вычисления разности между наибольшим и наименьшим двузначными числами
def process_number(N):
    digits = [int(digit) for digit in str(N)]
    # Находим наибольшее и наименьшее возможное двузначное число
    digits.sort()

    # Наименьшее двузначное число не может начинаться с нуля, поэтому переставляем цифры
    if digits[0] == 0:
        min_num = digits[1] * 10 + digits[0]
    else:
        min_num = digits[0] * 10 + digits[1]

    # Наибольшее двузначное число
    max_num = digits[2] * 10 + digits[1]

    return max_num - min_num


# Основной цикл по числам на отрезке [300; 400]
count = 0
for N in range(300, 400):
    if process_number(N) == 20:
        count += 1

print(count)
