from math import isqrt

max_xy = 0
max_dec = 0
for x in range(57):
    for y in range(57):
        number = 5 * 10**7 + 3 * 10**6 + x * 10**5 + 6 * 10**4 + 6 * 10**3 + y * 10**2 + 3 * 10 + 5

        # print(number)
        if number % 56 == 0:
            xy_number = y * 10**1 + x
            #print(number, xy_number)

            if isqrt(xy_number)**2 == xy_number:
                if xy_number > max_xy:
                    max_xy = xy_number
                    max_dec = xy_number

                    print(max_xy, max_dec)
