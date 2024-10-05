import ipaddress as ip

count = 0
arr = [1, 3, 7, 15, 31, 63, 127, 255]
ips = ip.ip_network(f'202.75.38.160/255.255.255.240', False)

ans = 0

for ip_ in ips:
    bins_ = bin(int(ip_))[2:]
    if '111' in bins_:
        ans += 1


print(ans)