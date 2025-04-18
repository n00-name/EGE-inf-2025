count = 0
max_num = 0

for num in range(3201, 12877):  # 12876 включительно
    if num % 4 == 0 and num % 7 != 0 and num % 11 != 0 and num % 13 != 0 and num % 19 != 0:
        count += 1
        max_num = num  # Последнее подходящее число будет максимальным

print(count, max_num)
