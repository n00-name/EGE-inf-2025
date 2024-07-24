def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


def main():
    for n in range(1, 100):
        s = '>' + '1' * 11 + '2' * n + '3' * 11

        while '>1' in s or '>2' in s or '>3' in s:
            if '>1' in s:
                s = s.replace('>1', '222>')
            elif '>2' in s:
                s = s.replace('>2', '3>')
            elif '>3' in s:
                s = s.replace('>3', '1>')

        s = s[:-1]
        summ = sum(list(map(int, s)))
        print(summ)

        f = is_prime(summ)
        if f:
            print(n)
            break


main() # ans 2
