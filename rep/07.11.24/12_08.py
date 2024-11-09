from itertools import permutations


def count_valid_numbers():
    # Возможные цифры в восьмеричной системе, исключая 4
    digits = ['0', '1', '2', '3', '5', '6', '7']
    count = 0

    # Генерация всех 6-значных восьмеричных чисел с ровно двумя '4'
    for perm in permutations(digits, 4):
        # Формируем кандидат с двумя '4' между другими уникальными цифрами
        candidate = list(perm)
        candidate.insert(0, '4')
        candidate.insert(3, '4')

        # Проверяем, удовлетворяет ли кандидат всем условиям
        # Между двумя '4' (позиции 1 и 4) цифры должны быть >= 5
        middle_digits = [candidate[1], candidate[2]]
        if all(int(digit) >= 5 for digit in middle_digits):
            count += 1

    return count


valid_number_count = count_valid_numbers()
print(valid_number_count)
