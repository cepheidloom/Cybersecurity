from scapy.layers.l2 import Ether, ARP, srp


def arpscan_getmac(ip: str) -> list[tuple[str, str]]:
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = ARP(pdst=ip)
    answer_list, _ = srp(broadcast / arp_request, timeout=1, verbose=True)

    answer_list.summary(
        lambda send, rev: rev.sprintf(
            "\n#### Response ####\n%Ether.src%  |  %ARP.psrc%"
        )
    )
    mac_ip = [(answer[1].hwsrc, answer[1].psrc) for answer in answer_list]

    return mac_ip


if __name__ == "__main__":
    arpscan_getmac("192.168.29.1")
