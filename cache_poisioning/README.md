We will be using docker to simulate cache poisoning attacks instead of tiresome and slow virtual machines.

1. First install Docker on you system. The steps shown on the official site are easy and clear.
https://docs.docker.com/engine/install/

2. Using Docker, we are going to create 2 containers. Container1 will act as the victim and container2 will act as the attacker.
3. First we create a shared network on which the 2 containers will be able to communicate. Type the below command in your terminal
```bash
docker network create --driver bridge mynetwork
```
> This creates a new network using Docker's bridge driver. Containers on this network will be able to communicate with each other.

4. Below command start a new container which we name as container1 , we attach it to mynetwork that we created above and it is based on a ubuntu image . A bash shell is started inside the container. Note that you will seemingly enter a new terminal with a new username starting with root.
```bash
docker run -it --network=mynetwork --name container1 ubuntu bash
```

5. Similarly we create another container named container2 that acts as attacker in this experiment.
```bash
docker run -it --network=mynetwork --name container2 ubuntu bash
```

6. Keep both these containers open in 2 terminals at the same time, then type these following commands in both the terminals of container1 and container2
```bash
apt-get update
apt-get install -y arping python3-scapy
```
This installs python3 and scapy in our containers

7. If you press exit in any of the container terminals, you will exit the terminal and the container will close. If you want to start that container again, just enter 
```
docker start -ai <container-name>
```

8. You can either remember the container names or get the container names using the following command
```bash
docker ps
```
for running containers, and 
```bash
docker ps -a
```
for all containers, including stopped ones

9. Now install the following tools in both the containers
```bash
apt-get update
apt-get install -y iproute2
apt-get install -y net-tools
```
These tools will install arp and ip commands in both the containers respectively.

10. Now type the following command to get the ip and mac address of each container
```bash
ip addr show eth0
```
11. Now you have both the ip and mac address of container1 and container2. Since we want to simulate container1 as the victim and container2 as the attacker, we fill the following variables in the repo script as mentioned:
```python
#!/usr/bin/env python3

from scapy.all import *

# Victim (container1)
IP_target = "172.17.0.2" //ip address of container1
MAC_target = "02:42:ac:11:00:02" //mac address of container1

# Attacker (container2)
IP_spoofed = "172.18.0.3" //ip address of container2
MAC_spoofed = "02:42:ac:12:00:03" //mac address of container2
```

12. We run the script in container2 using python3.

Thanks you :) 
By @cepheidloom and @FlareXes