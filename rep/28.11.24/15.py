for a in range(1, 1000):
    if all(((2*x+3*y <= 95) and (x >= a) and (y >= a)) == False for x in range(0,1000) for y in range(0,1000)):
        print(a)
        break