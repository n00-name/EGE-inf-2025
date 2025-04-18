import math

def count_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

found_numbers = []
for num in range(118811, 118973):
    divisors = count_divisors(num)
    if len(divisors) == 6:
        found_numbers.append(divisors)
        if len(found_numbers) == 3:
            print("Третий найденный номер:", num)
            print("Его делители:", *divisors)
            break
