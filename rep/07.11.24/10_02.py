print('x y z w F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = (w or x or y) <= (((y or z) and x) or (y and (w or z)))

                if not f:
                    print(x, y, z, w, int(f))