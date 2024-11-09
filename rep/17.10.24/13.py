import ipaddress as ip

ips = ip.ip_network(f'136.157.177.128/255.255.255.252', False)

for ip_ in ips:
    ip_bin = bin(int(ip_))[2:]

    if ip_bin.count('0') % 2 == 0:
        print(ip_bin)

