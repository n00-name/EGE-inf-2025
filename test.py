def replace_letters(input_str):
    # Словарь с заменами: A -> ".", B -> "-", C -> " "
    replacements = {'A': '.', 'B': '-', 'C': ' '}

    # Проходим по каждой букве строки и подставляем замену
    result = ''.join(replacements.get(char, char) for char in input_str)

    return result


# Пример использования
input_str = "AABACABAACABCABCABCABCABCABCABCABCAAAA"
output_str = replace_letters(input_str)
print(output_str)
