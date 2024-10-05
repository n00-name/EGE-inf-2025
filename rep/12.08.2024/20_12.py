def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


for n in range(1, 100):

    s = '>' + '1' * 23 + '2' * n + '3' * 25

    while '>1' in s or '>2' in s or '>3' in s:

        if '>1' in s:
            s = s.replace('>1', '1>')
        if '>2' in s:
            s = s.replace('>2', '>3')
        if '>3' in s:
            s = s.replace('>3', '>11')

    s = s[:-1]
    suma = sum(map(int, s))
    if is_prime(suma):
        print(n, suma)  # 3
        break
