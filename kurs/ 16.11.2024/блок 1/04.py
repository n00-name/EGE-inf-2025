from itertools import permutations

res = set()
soglasnye = set("МФБРХ")  # Согласные (кроме Й)

for perm in permutations("АМФИБРАХИЙ"):
    word = ''.join(perm)
    # Проверяем условие: на четных позициях стоят согласные (кроме Й)
    if all(word[i] in soglasnye for i in range(1, len(word), 2)):  # Четные позиции (индексация с 0)
        res.add(word)

print(len(res))
