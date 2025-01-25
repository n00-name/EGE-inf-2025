print('w x y z f')
for w in (0, 1):
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):

                f = (x <= y) and (z == (w <= x)) and (not w)

                if f:
                    print(w, x, y, z, int(f))