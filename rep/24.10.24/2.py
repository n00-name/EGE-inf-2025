def calculate_F(n):
    # Создаем список достаточно большого размера, чтобы включить все значения до n+1
    F_values = [0] * (900001 + 1)  # Делаем список длиной 900002 (до 900001 включительно)

    # Заполняем значения для F(n), начиная с n и двигаясь вниз
    for i in range(900001, 900000, -1):
        F_values[i] = i**2

    for i in range(900000, 0, -1):
        F_values[i] = 2 * i - F_values[i + 1]

    return F_values

# Вычисляем значения F(100) и F(98)
F_values = calculate_F(100)
result = F_values[100] - F_values[98]

print(result)
