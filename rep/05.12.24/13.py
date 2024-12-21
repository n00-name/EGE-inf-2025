import ipaddress

# Дадим исходные данные
network_address = "94.149.96.0"
subnet_mask = "255.255.224.0"

# Получаем объект сети, используя ipaddress
network = ipaddress.IPv4Network(f'{network_address}/{subnet_mask}', strict=False)

# Функция для подсчета единичных бит в двоичной записи числа
def count_ones_in_binary(ip):
    binary_ip = bin(int(ip))[2:]  # Переводим IP в двоичную строку без префикса '0b'
    return binary_ip.count('1')

# Функция для проверки, заканчивается ли строка на '11'
def ends_with_11(ip):
    binary_ip = bin(int(ip))[2:]
    return binary_ip.endswith('11')

# Ищем все адреса в сети, которые удовлетворяют условиям
valid_ips = []

for ip in network:
    if count_ones_in_binary(ip) % 3 == 0 and ends_with_11(ip):
        valid_ips.append(str(ip))

# Выводим результат
print(f"Количество подходящих IP-адресов: {len(valid_ips)}")
