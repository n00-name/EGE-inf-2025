from ipaddress import ip_network


network = ip_network("142.108.56.118/255.255.255.240", strict=False)
count = 0

for ip in network:  # Перебираем только допустимые IP-адреса
    binary_ip = f"{int(ip):032b}"
    left_ones = binary_ip[:16].count('1')
    right_ones = binary_ip[16:].count('1')

    if left_ones < right_ones:
        count += 1

print(count)
