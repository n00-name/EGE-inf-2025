def main():
    maxx = -1
    for n in range(4, 10_000):
        s = '1' + '2' * n

        while '12' in s or '322' in s or '222' in s:
            if '12' in s:
                s = s.replace('12', '2', 1)
            if '322' in s:
                s = s.replace('322', '21', 1)  # Исправлено: убраны лишние пробелы
            if '222' in s:
                s = s.replace('222', '3', 1)

        summ = sum(list(map(int, s)))

        if summ:
            maxx = max(maxx, summ)
            print(maxx, n)

main()  # ans 2
