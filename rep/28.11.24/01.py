print('x y z w F')
for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                f = (w != y) or (not x) or (z and w)

                if not f:
                    print(x, y, z, w, int(f))