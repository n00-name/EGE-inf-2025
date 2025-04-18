def process_number(n):
    digits = [int(digit) for digit in str(n)]

    sum1 = digits[0] + digits[3]
    sum2 = digits[1] + digits[2]

    return int(f"{sum2}{sum1}")


for num in range(9999, 999, -1):
    if process_number(num) == 815:
        print(f"Исходное число: {num}")
        break