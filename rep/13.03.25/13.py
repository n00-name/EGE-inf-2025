from ipaddress import ip_network


network = ip_network("222.121.128.0/255.255.224.0", strict=False)
count = 0

for ip in network:  # Перебираем только допустимые IP-адреса
    binary_ip = f"{int(ip):032b}"
    left_ones = binary_ip[-2:]
    count += 1


    print(binary_ip, left_ones)

print(count / 4)