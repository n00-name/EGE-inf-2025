def main():
    count = 0
    for n in range(6, 6000):
        s = '3' + '4' * n

        while '44444' in s or '4544' in s or '344' in s:
            if '44444' in s:
                s = s.replace('44444', '45', 1)
            elif '4544' in s:
                s = s.replace('4544', '344', 1)
            else:
                s = s.replace('344', '3')

        summ = sum(list(map(int, s)))

        if summ == 5566:
            count += 1
            print(count, n)


main() # ans 2
