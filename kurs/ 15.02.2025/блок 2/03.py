# Функция для поиска наименьшего пятизначного числа
def find_min_number():
    # Перебираем все возможные значения цифр
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                for a4 in range(10):
                    for a5 in range(10):
                        # Суммы по правилам задачи
                        sum1 = a1 + a3 + a5
                        sum2 = a2 + a4

                        # Получаем результат в виде строки, отсортировав суммы
                        result = ''.join(sorted([str(sum1), str(sum2)]))

                        # Если результат 621, возвращаем число
                        if result == "621":
                            return f"{a1}{a2}{a3}{a4}{a5}"


# Ищем минимальное число
min_number = find_min_number()
print(min_number)
