from ipaddress import ip_network

count = 0
ans = 0
for ip in ip_network('216.130.64.0/255.255.192.0'):
    lst = str(ip).split('.')
    lst = list(map(int, lst))
    ifchet = [1 if x % 2 == 0 else 0 for x in lst]
    print(ifchet)
    count += 1
    if sum(ifchet) == 4:
        ans += 1
print(count, ans)
