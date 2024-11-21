# Solution to the problem
from itertools import product

# Define the parameters
base = 13  # base of the numeral system
length = 5  # length of the number (5 digits)

# Even and odd digits in base-13 system
even_digits = {'0', '2', '4', '6', '8', 'A', 'C'}
odd_digits = {'1', '3', '5', '7', '9', 'B'}


# Function to check the conditions
def is_valid(number):
    # Convert to base-13 representation as string and check for only one '2'
    if number.count('2') != 1:
        return False

    # Check that no two even or two odd digits are adjacent
    for i in range(len(number) - 1):
        if (number[i] in even_digits and number[i + 1] in even_digits) or \
                (number[i] in odd_digits and number[i + 1] in odd_digits):
            return False

    return True


# Generate all possible 5-digit numbers in base-13
valid_numbers = 0
for digits in product('0123456789ABC', repeat=length):
    number = ''.join(digits)
    if is_valid(number):
        valid_numbers += 1

print(valid_numbers)