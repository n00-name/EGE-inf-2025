import base64


def encode_base64_100_times(input_string):
    encoded = input_string.encode('utf-8')  # Преобразуем строку в байты
    cnt = 0
    for _ in range(61):
        print(cnt)
        if cnt == 10:
            encoded = base64.b85encode(encoded)  # Кодируем в base85 на 10-й итерации
        else:
            encoded = base64.b64encode(encoded)  # Кодируем в base64

        cnt += 1

    return encoded.decode('utf-8')  # Возвращаем результат как строку


# Пример использования:
input_string = 'ZOV'
encoded_string = encode_base64_100_times(input_string)

with open('output_bytes.txt', 'w') as file:
    file.write(encoded_string)
