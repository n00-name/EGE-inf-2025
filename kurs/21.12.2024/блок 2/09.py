def count_programs(start, end, target):
    # Проверка, содержит ли число target
    def contains(number, target):
        return str(target) in str(number)

    def f(current, target_met):
        # Если достигли конечного числа
        if current == end:
            # Учитываем только те пути, где встречалось число 12
            return 1 if target_met else 0
        if current > end:
            return 0
        # Проверяем, было ли число 12 на пути
        target_met = target_met or contains(current, target)
        # Рекурсивно пробуем все три команды
        return (
                f(current + 2, target_met) +  # Команда 1: прибавить 2
                f(current + 3, target_met) +  # Команда 2: прибавить 3
                f(int(str(current) + "1"), target_met)  # Команда 3: дописать "1" справа
        )

    return f(start, False)


# Стартовое число: 3, конечное число: 25, промежуточное число: 12
result = count_programs(3, 25, 12)
print(result)
