print('x y z w F1 F2')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f1 = (w <= y) == (z <= x)
                f2 = (w <= y) and ((not x) == z)


                print(x, y, z, w, int(f1), int(f2))