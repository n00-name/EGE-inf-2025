print('x y z F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = (x and y) or ((not x) and (not z))
            if f:
                print(x, y, z, int(f))
