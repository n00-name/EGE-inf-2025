s = 8 ** 148 - 4 ** 123 + 2 ** 654 - 17

bin_s = bin(s)[2:]
print(bin_s.count('1'))