import ipaddress as ip

count = 0
ips = ip.ip_network('102.141.0.0/255.255.192.0', False)

for ip_ in ips:
    bite = bin(int(ip_))[2:]

    if bite.count('1') % 7 == 0 and bite[-4:] == '1011':
        print(bite)
        count += 1
print(count)
