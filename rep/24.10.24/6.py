import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def main():
    for n in range(2, 10_000):
        s = '>' + '0' * 21 + '1' * n + '2' * 11

        while '>1' in s or '>2' in s or '>0' in s:
            if '>1' in s:
                s = s.replace('>1', '22>', 1)
            if '>2' in s:
                s = s.replace('>2', '2>', 1)
            if '>0' in s:
                s = s.replace('>0', '1>', 1)

        s = s[:-1]  # Убираем последний символ '>'
        summ = sum(list(map(int, s)))

        if is_prime(summ):  # Проверяем, является ли сумма простым числом
            print(n)
            break

main()
