from itertools import product

count = 0
for s in product("0123456789ABCDE", repeat=5):
    if s.count("8") == 1 and s[0] != "0":  # Ровно одна цифра 8 и число не начинается с 0
        # Считаем цифры, превышающие 9 (A, B, C, D, E, F)
        high_digits = s.count("A") + s.count("B") + s.count("C") + s.count("D") + s.count("E") 
        if high_digits >= 2:  # Не менее двух таких цифр
            count += 1

print(count)
