def F(n):
    values = {2024: 1, 2025: 2}  # Initialize F(2024) = 1
    for i in range(2025, n + 1):
        values[i] = 2  # F(n) = 2 for all n > 2024

    for i in range(2023, 0, -1):  # Compute F(n) from 2023 down to 1
        values[i] = i * (i + 1) + values[i + 1] - values[i + 2]

    return values[n]

# Calculate the expression F(100) - F(10) + F(2020)
result = F(100) - F(10) + F(2020)
print(result)
