# more information here
# https://realpython.com/python-ipaddress-module/
from ipaddress import IPv4Address, IPv4Network


class NetworkIP:
    def __init__(self, ip, mask=None):
        if not "/" in ip:
            ip = f"{ip}/{mask}"
        self.network = IPv4Network(ip, False)

    def list_ips_in_network(self):
        for ip in self.network.hosts():
            yield ip

    def __iter__(self):
        yield from self.list_ips_in_network()

    def is_ip_in_network(self, ip: str):
        return IPv4Address(ip) in self.network

    def __contains__(self, ip: str):
        return self.is_ip_in_network(ip)


def main():
    ip = "192.168.0.1"
    mask = "255.255.255.0"
    network = NetworkIP(ip, mask)
    for ip in network.list_ips_in_network():
        print(ip)
    test_ip = "192.168.1.134"
    test_ip2 = "192.168.0.54"
    print(f"Is {test_ip} in the subnetwork? {network.is_ip_in_network(test_ip)}")
    print(f"Is {test_ip2} in the subnetwork? {test_ip2 in network}")

    print("============== CIDR testing =============")
    ip = "192.168.0.1/21"
    network = NetworkIP(ip)
    for ip in network:
        print(ip)
    test_ip = "192.168.1.134"
    test_ip2 = "192.168.0.54"
    print(f"Is {test_ip} in the subnetwork? {network.is_ip_in_network(test_ip)}")
    print(f"Is {test_ip2} in the subnetwork? {network.is_ip_in_network(test_ip2)}")


if __name__ == "__main__":
    main()
