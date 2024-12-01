with open('17_02_402.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Найдем минимальное двузначное число, которое кратно сумме своих цифр
def digit_sum(n):
    return sum(int(d) for d in str(n))

min_valid_number = float('inf')
for num in nums:
    if 10 <= num <= 99 and num % digit_sum(num) == 0:
        min_valid_number = min(min_valid_number, num)

# Перебор пар подряд идущих чисел
count = 0
max_sum = float('-inf')

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if a % min_valid_number == 0 or b % min_valid_number == 0:
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)
