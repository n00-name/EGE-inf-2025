for x in '0123456789ABCDEF':

    s1 = int(f'1234{x}') + 5
    s2 = int(f'12{x}34') + 5

    f = s1 + s2
    if f % 14 == 0:
        print(f/14)