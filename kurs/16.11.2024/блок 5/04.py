import string

def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


x = string.digits + string.ascii_uppercase
y = string.digits + string.ascii_uppercase

x = x[1:12]
y = y[1:19]
print(x, y)
for i in x:
    for j in y:

        s1 = '5' + i + '9' + i + '4'
        s2 = '7' + 2 * i + '6'
        s3 = '55' + 2 * i + '8'
        s4 = '3' + j + i + '7'

        f = int(s1, 12) + int(s2, 14) + int(s3, 16) - int(s4, 19)
        if is_prime(f):
            print(i, j)