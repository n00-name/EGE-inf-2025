def max_valid_triples(filename):
    with open(filename, 'r') as f:
        s = f.read().strip()

    max_count = 0
    count = 0
    i = 0
    while i + 2 < len(s):
        triplet = s[i:i+3]
        if triplet == 'NPO' or triplet == 'PNO':
            count += 1
            i += 3
            max_count = max(max_count, count)
        else:
            count = 0
            i += 1  # Двигаемся на 1, чтобы не пропустить возможный сдвиг

    return max_count

print(max_valid_triples('24-4.txt'))
