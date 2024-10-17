print('x y z F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = (y <= x) and (z <= y)

            print(x, y, z, int(f))
