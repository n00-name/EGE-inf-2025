def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x: int) -> int:
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and is_prime(i) and i != 2 and i != 3 and i != 5 and i != 7 and i != 11 and i != 13 and i != 17 and i != 19:
            return i
    return 0


lst = []
arr = []
for num in range(523456, 578925 + 1):

    n1 = f(num)
    if n1 != 0:
        n2 = num // n1
        ans = abs(n2 - n1)

        if ans != 0:
            lst.append(ans)
            arr.append([n1, n2])


minn = min(lst)
ind = lst.index(minn)

print(*arr[ind])