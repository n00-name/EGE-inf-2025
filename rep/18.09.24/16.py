start = 2025
cache = {n: n for n in range(start, 2025 + 10)}
print(cache)
# Fill cache iteratively for the required range
for i in range(2024, 14, -1):
    cache[i] = cache[i + 1] - cache[i + 2] + 7

# Now you can access f(15) and f(24) from the cache
result = cache[15] - cache[24]
print(result)
