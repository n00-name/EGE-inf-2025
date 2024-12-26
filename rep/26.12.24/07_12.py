for n in range(9999, 2, -1):
    s = '2' + '7' * n
    z = 1  # Начинаем с 1 для корректного вычисления произведения
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        elif '777' in s:  # Используем elif для корректности обработки
            s = s.replace('777', '3', 1)
        elif '377' in s:
            s = s.replace('377', '73', 1)

    lst = list(map(int, s))
    for dig in lst:
        z *= dig  # Умножаем каждую цифру на текущее значение z
    if z % 3 == 0 and z % 10 == 1:
        print(n)
