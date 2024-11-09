count = 0
for x1 in "2468":
    for x2 in "012345678":
        for x3 in "012345678":
            for x4 in "012345678":
                for x5 in "012345678":
                    for x6 in "0145678":
                        s = x1+x2+x3+x4+x5+x6
                        if s.count("1") >= 2:
                            count += 1
print(count)