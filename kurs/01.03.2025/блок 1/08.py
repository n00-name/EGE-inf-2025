from ipaddress import ip_network

# Определяем сетевой адрес с маской
network = ip_network("211.48.136.64/255.255.255.224", strict=False)
count = 0

# Перебираем все IP-адреса в сети
for ip in network:
    binary_ip = f"{int(ip):032b}"  # Преобразуем IP в двоичный формат

    if binary_ip[-2:] == '11':
        count += 1

print(count)
