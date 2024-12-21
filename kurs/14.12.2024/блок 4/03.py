print('a b c d f')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):

                f = (a <= b) and (b != c) and (d <= a)
                if f:
                    print(a, b, c, d, int(f))