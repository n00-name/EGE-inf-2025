import string

# Function to convert a number from base 'b' to base 10
def to10(num_str, base):
    alph = string.digits + string.ascii_uppercase
    num10 = 0
    for digit in num_str:
        num10 = num10 * base + alph.index(digit)
    return num10

# Check different bases from 2 to 30
for x in range(2, 30):
    # Convert numbers in base 'x' to base 10 and check the equation
    try:
        if to10('12', x) * to10('33', x) == to10('406', x):
            print(f"Base: {x}")
    except ValueError:
        # In case of invalid digits for a base, just skip
        continue


import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return int(s[::-1])

for x in range(1, 30):
    f = to10(12, x) * to10(33, x) == to10(406, x)


    if f:
        print(x)

