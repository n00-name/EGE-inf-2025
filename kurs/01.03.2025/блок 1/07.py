from ipaddress import ip_network

# Определяем сетевой адрес с маской
network = ip_network("192.168.248.176/255.255.255.240", strict=False)
count = 0

# Перебираем все IP-адреса в сети
for ip in network:
    binary_ip = f"{int(ip):032b}"  # Преобразуем IP в двоичный формат
    count_0 = binary_ip.count("0")
    count_1 = binary_ip.count("1")

    if count_0 == count_1:  # Если количество единиц и нулей одинаково
        count += 1

print(count)
