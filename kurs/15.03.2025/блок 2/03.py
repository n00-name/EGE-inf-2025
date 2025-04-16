
def f(n):
    s = ''
    while n > 0:
        s = s + str(n % 8)
        n = n // 8
    return s[:1] == '3'



with open('17-1.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))
print(nums)

for i in range(0, len(nums) - 1):
    duo = nums[i:i + 2]
    # print(duo)

    if_del_na_9 = ['1' if x % 9 == 1 else '0' for x in duo]
    if_del_na_9 = ''.join(if_del_na_9)
    # print(if_del_na_9)
    s1 = duo[0]
    s2 = duo[1]
    if '01' in if_del_na_9 and f(s1) or '10' in if_del_na_9 and f(duo[1]):
        print(duo)