with open("17var05.txt") as f:
    numbers = list(map(int, f.readlines()))

# Находим минимальный элемент последовательности, оканчивающийся на 25
min_ending_25 = min([num for num in numbers if num % 100 == 25], default=float("inf"))

count = 0
max_sum = 0

# Перебираем тройки подряд идущих элементов
for i in range(len(numbers) - 2):
    triplet = numbers[i:i + 3]
    sum_triplet = sum(triplet)

    # Проверяем условие: только одно число двузначное
    double_digit_count = sum(10 <= x < 100 for x in triplet)

    if double_digit_count == 1 and sum_triplet < min_ending_25:
        count += 1
        max_sum = max(max_sum, sum_triplet)

print(count, max_sum)
