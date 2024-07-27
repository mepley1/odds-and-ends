# Get IPv4 addresses of all network interfaces

import netifaces

def get_ip_addresses():
    ip_addresses = []
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for link in addresses[netifaces.AF_INET]:
                ip_addresses.append(link['addr'])

    return ip_addresses

if __name__ == "__main__":
    ips = get_ip_addresses()
    for ip in ips:
        print(ip)
