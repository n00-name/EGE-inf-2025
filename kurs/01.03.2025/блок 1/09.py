from ipaddress import ip_network

# Определяем сетевой адрес с маской
network = ip_network("184.178.54.144/255.255.255.240", strict=False)
count = 0

# Перебираем все IP-адреса в сети
for ip in network:
    binary_ip = f"{int(ip):032b}"  # Преобразуем IP в двоичный формат

    if '111' in binary_ip:
        count += 1

print(count)
