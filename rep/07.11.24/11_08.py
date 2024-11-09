import itertools

# Алфавит языка Ротокас
alphabet = ['A', 'E', 'G', 'I', 'K', 'O', 'P', 'R', 'S', 'T', 'U', 'V']

# Функция для проверки, является ли перестановка деранджментом
def is_derangement(perm):
    return all(perm[i] != alphabet[i] for i in range(len(alphabet)))

# Генерация всех возможных перестановок и подсчет деранджментов
derangements_count = sum(1 for perm in itertools.permutations(alphabet) if is_derangement(perm))

print("Количество деранджментов:", derangements_count)
