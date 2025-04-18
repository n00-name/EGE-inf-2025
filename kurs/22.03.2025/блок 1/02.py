with open("24.txt", "r") as file:
    s = file.readline().strip()

arr = s.split("CD")
maxi = 0

for i in range(len(arr) - 160):
    sm = len("".join(arr[i:i+161]))
    if i != 0:
        sm += 1
    if i != len(arr) - 161:
        sm += 1
    maxi = max(maxi, sm + 320)

print(maxi)