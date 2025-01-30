from sympy import symbols, Eq, simplify, solve

# Define the base N and the sum of digits
N = symbols('N', integer=True)
sum_of_digits = 75

# Define the expression in terms of N
value = N**25 - 2 * N**13 + 10

# Sum of digits equation
def digit_sum_equation(value, base, target_sum):
    result = 0
    while value > 0:
        result += value % base
        value //= base
    return result - target_sum

# Solve for N where the digit sum equals the target
solution = solve(digit_sum_equation(value, N, sum_of_digits), N)
print(solution)