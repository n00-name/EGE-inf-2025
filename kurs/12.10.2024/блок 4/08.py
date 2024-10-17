print('x y z w F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = (not w) and z and (y <= x)

                if f:
                    print(x, y, z, w, int(f))
