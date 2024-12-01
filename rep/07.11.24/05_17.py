# Reading the data from '17_01_411.txt' file
with open('17-411.txt') as file:
    sequence = list(map(int, file.read().split()))

# Step 2: Identify the maximum element that ends with 1
max_elem_ending_with_1 = max([x for x in sequence if x % 10 == 1])

# Initialize counters
count_quads = 0
min_sum_quad = float('inf')

# Step 3: Iterate through each consecutive group of 4 elements
for i in range(len(sequence) - 3):
    quad = sequence[i:i+4]
    if all(x < max_elem_ending_with_1 for x in quad):
        even_count = sum(1 for x in quad if x % 2 == 0)
        if even_count % 2 == 1:
            count_quads += 1
            min_sum_quad = min(min_sum_quad, sum(quad))

print(count_quads, min_sum_quad)
