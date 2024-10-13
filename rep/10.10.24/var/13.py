from ipaddress import *
ips = ip_network('106.184.0.0/255.248.0.0', 0)
cnt = 0
for ip in ips:
    s = f'{ip:b}'
    print(s)
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)