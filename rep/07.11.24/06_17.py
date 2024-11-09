# Read data from '17-411.txt' file
with open('17-411.txt') as file:
    sequence = list(map(int, file.read().split()))

# Step 1: Identify the minimum element that is a multiple of 3
min_elem_multiple_of_3 = min([x for x in sequence if x % 3 == 0])

# Step 2: Identify the maximum element that ends with 3
max_elem_ending_with_3 = max([x for x in sequence if x % 10 == 3])

# Initialize counters
count_pairs = 0
min_sum_square_pairs = float('inf')

# Step 3: Iterate through each consecutive pair of elements
for i in range(len(sequence) - 1):
    pair = sequence[i:i+2]
    conditions_met = [
        min_elem_multiple_of_3 <= x <= max_elem_ending_with_3 for x in pair
    ]
    if sum(conditions_met) == 1:  # Exactly one element meets the condition
        count_pairs += 1
        sum_of_squares = pair[0] ** 2 + pair[1] ** 2
        min_sum_square_pairs = min(min_sum_square_pairs, sum_of_squares)

print(count_pairs, min_sum_square_pairs)
