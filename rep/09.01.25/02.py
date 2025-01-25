def convert_to_decimal_with_powers(number, base):
    """Переводит число из системы счисления с основанием base в десятичную через суммы произведений."""
    values = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    decimal_value = 0
    power = len(number) - 1  # Начинаем с самой старшей степени

    for char in number:
        decimal_value += values[char] * (base ** power)
        power -= 1

    return decimal_value

def find_max_x_and_calculate():
    base = 153
    divisible_by = 152
    max_x = None
    result = None

    for x in range(base):  # Возможные значения x
        # Представляем числа в явной форме с учетом степеней
        try:
            num1 = (
                11 * (base ** 8)  # B
                + 10 * (base ** 7)  # A
                + x * (base ** 6)  # x
                + 9 * (base ** 5)  # 9
                + 8 * (base ** 4)  # 8
                + 10 * (base ** 3)  # A
                + 13 * (base ** 2)  # D
                + 15 * (base ** 1)  # F
            )

            num2 = (
                12 * (base ** 7)  # C
                + 1 * (base ** 6)  # 1
                + x * (base ** 5)  # x
                + 7 * (base ** 4)  # 7
                + 8 * (base ** 3)  # 8
                + 10 * (base ** 2)  # A
                + 7 * (base ** 1)  # 7
                + 5 * (base ** 0)  # 5
            )

            # Проверяем делимость произведения на divisible_by
            if (num1 * num2) % divisible_by == 0:
                max_x = x
                result = (
                    5 * (base ** 2)  # 5
                    + x * (base ** 1)  # x
                    + 10 * (base ** 0)  # A
                )
        except Exception as e:
            continue

    return max_x, result

max_x, result = find_max_x_and_calculate()
print(f"Максимальное значение x: {max_x}")
print(f"Значение 5xA в десятичной системе: {result}")
