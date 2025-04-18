with open("24.txt", "r") as file:
    data = file.read().strip()

alwd = set("ABEF")
mx = 0
length = 0

for char in data:
    if char in alwd:
        length += 1
        mx = max(mx, length)
    else:
        length = 0

print(mx)
