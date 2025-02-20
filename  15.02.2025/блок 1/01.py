def process_number(n):
    digits = [int(digit) for digit in str(n)]

    sum1 = digits[0] + digits[1]
    sum2 = digits[2] + digits[3]

    return int(f"{sum2}{sum1}")


for num in range(1000, 10000):
    if process_number(num) == 1512:
        print(f"Исходное число: {num}")
        break

