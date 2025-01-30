for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):

                f = (x and (not y)) or (x == z)

                if not f:
                    print(x, y, w, z, int(f))