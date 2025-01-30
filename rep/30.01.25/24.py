def min_substring_with_a(filename):
    with open(filename, 'r') as file:
        s = file.read().strip()

    target_count = 2024
    min_length = float('inf')
    left = 0
    count_a = 0

    for right in range(len(s)):
        if s[right] == 'A':
            count_a += 1

        while count_a == target_count:
            min_length = min(min_length, right - left + 1)
            if s[left] == 'A':
                count_a -= 1
            left += 1

    return min_length if min_length != float('inf') else -1


# Замените 'file1.txt' на имя вашего файла
filename = '24var05.txt'
result = min_substring_with_a(filename)
print("Минимальная длина последовательности:", result)
