import ipaddress as ip

found = False
min_b = None

for i in range(0, 9):
    b = int('1' * i + '0' * (8 - i), 2)
    ips = ip.ip_network(f"252.63.194.3/255.255.{str(b)}.0", False)
    condition_met = True

    for ip_ in ips:
        bins_ = bin(int(ip_))[2:]
        a = bins_[:16]
        aa = bins_[16:]

        if not (a.count('1') >= aa.count('1')):
            condition_met = False
            break

    if condition_met:
        found = True
        min_b = b
        break

if found:
    print(f"Found the minimum b: {min_b}")
else:
    print("No such b found.")