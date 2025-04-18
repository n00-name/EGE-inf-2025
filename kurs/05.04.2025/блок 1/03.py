with open("24-3.txt", "r") as file:
    text = file.read().strip()

max_len = 0
left = 0
dot_count = 0

for right in range(len(text)):
    if text[right] == '.':
        dot_count += 1

    while dot_count > 4:
        if text[left] == '.':
            dot_count -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
