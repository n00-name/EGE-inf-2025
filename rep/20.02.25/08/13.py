from ipaddress import ip_network
ans = 0
for ip in ip_network('253.112.169.12/255.255.254.0', False):
    bin_ip = bin(int(ip))[2:]
    print(bin_ip)
    left = bin_ip[:16]
    right = bin_ip[16:]
    print(left, right)

    if right.count('1') >= left.count('1'):
        ans += 1

print(ans)