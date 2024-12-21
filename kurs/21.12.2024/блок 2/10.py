def count_trajectories(target, current=1, add_count=0, path=set(), numbers=set()):
    """
    Recursive function to count trajectories leading to target number.
    :param target: The final number to reach (70 in this case).
    :param current: Current number during the trajectory.
    :param add_count: Consecutive usage of addition (Add 3) command.
    :param path: Set of numbers to track the trajectory.
    :param numbers: Set of unique numbers encountered in valid trajectories.
    :return: Count of unique numbers in valid trajectories.
    """
    # Base case: if we reach the target exactly, validate trajectory
    if current == target:
        if 8 in path and 16 in path or 32 in path:  # Valid path condition
            numbers.update(path)
        return numbers

    # Base case: if current exceeds target, stop recursion
    if current > target:
        return numbers

    # Recursive case:
    # Apply multiplication (command 1)
    numbers = count_trajectories(target, current * 2, 0, path | {current}, numbers)

    # Apply addition (command 2), if not more than 2 consecutive additions
    if add_count < 2:
        numbers = count_trajectories(target, current + 3, add_count + 1, path | {current}, numbers)

    return numbers


# Run the function for the given problem
unique_numbers = count_trajectories(70)
print(len(unique_numbers), sorted(unique_numbers))  # Total count and list of unique numbers

p = []


def f(n, t, a):
    global p
    tmp_a = []
    for x in a:
        tmp_a.append(x)
    tmp_a.append(n)
    if n > t:
        return 0
    if n == t:
        p.append(tmp_a)
        return 1
    return f(2 * n, t, tmp_a) + f(n + 3, t, tmp_a)


f(2, 70, [])

# print(p) # Посмотреть на все траектории

p1 = []

for x in p:
    if not (8 in x and 16 in x and 32 in x):
        p1.append(x)

# print(p1) # Посмотреть на все траектории, которые не проходят одновременно через 8, 16 и 32

p2 = []

for x in p1:
    t = [b - a == c - b == d - c == 3 for a, b, c, d in zip(x, x[1:], x[2:], x[3:])]
    if not any(t):
        p2.append(x)

# print(p2) # Печать всех траекторий, удовлетворяющих условию задачи

s = set(x for y in p2 for x in y)

print(len(s))