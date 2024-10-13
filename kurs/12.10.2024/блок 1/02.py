print('x y z F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = (z or y) <= (x == z)

            if not f:
                print(x, y, z, int(f))
