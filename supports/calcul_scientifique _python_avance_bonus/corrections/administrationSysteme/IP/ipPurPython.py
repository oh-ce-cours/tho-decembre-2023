def ip_to_int(ip) -> int:
    ints = [int(part) for part in ip.split(".")]
    res = (
        (256 ** 3 * ints[0])
        + (256 ** 2 * ints[1])
        + (256 ** 1 * ints[2])
        + (256 ** 0 * ints[3])
    )
    return res


def int_to_ip(ipnum: int) -> str:
    part1 = int(ipnum / 256 ** 3) % 256
    part2 = int(ipnum / 256 ** 2) % 256
    part3 = int(ipnum / 256 ** 1) % 256
    part4 = int(ipnum / 256 ** 0) % 256
    return f"{part1}.{part2}.{part3}.{part4}"


def decimal_to_binary(decimal_int: int) -> str:
    return bin(decimal_int)[2:]


def binary_to_decimal(binary_str: str) -> int:
    return int(binary_str, 2)


def two_complement(binary_str: str) -> str:
    res = ""
    for letter in binary_str:
        if letter == "0":
            new_letter = "1"
        else:
            new_letter = "0"
        res += new_letter
    return res


def cidr_to_mask(cidr: str) -> str:
    number_of_1 = int(cidr)
    number_of_0 = 32 - number_of_1
    binary_ip = "1" * number_of_1 + "0" * number_of_0
    return int_to_ip(binary_to_decimal(binary_ip))


class NetworkIP:
    def __init__(self, ip, mask=None):
        if "/" in ip:
            parts = ip.split("/")
            ip = parts[0]
            cidr_mask = parts[1]
            mask = cidr_to_mask(cidr_mask)
        self.ip = ip
        self.mask = mask
        int_ip = ip_to_int(self.ip)
        int_mask = ip_to_int(self.mask)
        mask_invert = binary_to_decimal(two_complement(decimal_to_binary(int_mask)))

        self.first_ip_of_subnet = int_ip & int_mask
        self.last_ip_of_subnet = int_ip | mask_invert

    def list_ips_in_network(self):
        for decimal_ip in range(self.first_ip_of_subnet, self.last_ip_of_subnet + 1):
            yield int_to_ip(decimal_ip)

    def __iter__(self):
        yield from self.list_ips_in_network()

    def is_ip_in_network(self, ip: str):
        return self.first_ip_of_subnet < ip_to_int(ip) < self.last_ip_of_subnet

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
