def F(n):
    if n < 7:
        return 7
    elif n % 3 == 0:
        return 3 + F(n - 1)
    else:
        return 5 - F(n - 1)

# result = F(3015)
# print(result)


def F(n):
    values = {i: 7 for i in range(7)}  # Initialize values for n < 7 as 7
    for i in range(7, n + 1):
        if i % 3 == 0:
            values[i] = 3 + values[i - 1]
        else:
            values[i] = 5 - values[i - 1]
    return values[n]

result = F(3015)
print(result)
