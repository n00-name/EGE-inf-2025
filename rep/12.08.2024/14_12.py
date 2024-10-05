def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


for n in range(1, 100):

    s = '>' + '0' * 15 + '1' * n + '2' * 15

    # from random import shuffle; s = list(s); shuffle(s)

    while '>0' in s or '>1' in s or '>2' in s:

        if '>0' in s:
            s = s.replace('>0', '22>')
        if '>1' in s:
            s = s.replace('>1', '2>')
        if '>2' in s:
            s = s.replace('>2', '1>')

    s = s[:-1]
    suma = sum(map(int, s))
    if is_prime(suma):
        print(n, suma)  # 2
        break
