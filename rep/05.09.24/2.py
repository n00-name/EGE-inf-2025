def f(n):
    bin_ = bin(n)[2:]
    if sum(list(map(int, bin_))) % 2 == 0:
        bin_ = '11' + bin_[2:] + '00'
    else:
        bin_ = '10' + bin_[2:] + '11'

    ans = int(bin_, 2)
    return ans

lst = []

for n in range(1500):

    ans = f(n)
    ans = f(ans)

    print(ans)

    if ans > 1500:
        lst.append(ans)

print(min(lst))
