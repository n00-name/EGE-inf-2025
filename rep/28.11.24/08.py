from itertools import product

lst = [''.join(i) for i in product("ВЕЛОРУФ", repeat=8)]

print(lst.index("ОВЕРФЛОУ") + 1)


