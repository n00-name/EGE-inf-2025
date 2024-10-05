import ipaddress as ip

count = 0
ips = ip.ip_network(f'172.16.168.0/255.255.248.0', False)


for ip_ in ips:
    bin_ = bin(int(ip_))[2:]

    if bin_.count('1') % 5 != 0:
        count += 1

print(count)
