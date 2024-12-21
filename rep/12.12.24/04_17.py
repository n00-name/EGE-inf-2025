# Открываем файл и читаем данные
with open('17-411-4.txt', 'r') as f:
    nums = [int(x) for x in f.read().splitlines()]

# Находим максимальное число, которое заканчивается на 7
max_7 = max(num for num in nums if num % 10 == 7)

# Инициализируем переменные для подсчета количества пар и для максимальной суммы
count = 0
max_sum = 0

# Проходим по числам и ищем подходящие пары
for i in range(len(nums) - 1):
    num1, num2 = nums[i], nums[i + 1]

    # Проверяем условия задачи
    if (num1 // 100 == num2 // 100) and (num1 % 10 == 7 or num2 % 10 == 7) and (
            100 <= num1 <= 999 or 100 <= num2 <= 999):
        if num1 + num2 < max_7:
            count += 1
            max_sum = max(max_sum, num1 + num2)

# Выводим результат
print(count, max_sum)
