print('x y z F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = (x and y and (not z)) or (x and y and z) or (x and (not y) and (not z))

            if f:
                print(x, y, z, int(f))
