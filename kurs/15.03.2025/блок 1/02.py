count = 0
max_num = 0

for num in range(3439, 7411):  # 7410 включительно
    bin_last = num % 2
    hex_last = num % 6

    if bin_last != hex_last and (num % 9 == 0 or num % 10 == 0 or num % 11 == 0):
        count += 1
        max_num = num  # Последнее подходящее число будет максимальным

print(count, max_num)
