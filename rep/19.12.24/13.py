import ipaddress

# Define the network using ipaddress library
network = ipaddress.IPv4Network("79.128.96.0/255.255.224.0", strict=False)

# Variables to count matching IPs
count_matching_ips = 0

# Loop through all IPs in the network
for ip in network:
    # Convert IP to binary string
    binary_ip = f"{int(ip):032b}"
    print(binary_ip)

    # Check if binary ends with '100' and number of 1s is not divisible by 7
    if binary_ip.endswith("100") and binary_ip.count("1") % 7 != 0:
        count_matching_ips += 1

print(count_matching_ips)
