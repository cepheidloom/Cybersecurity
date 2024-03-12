*Today we are going to use snort to detect protocols between different source and destination address*

We are going to use a cap file name bgplu.
1. Download the bgplu.cap file from [packetlife.net](https://packetlife.net/captures/protocol/tcp/). You will see this file at the top of results. Then paste this file in the /volume directory of your systemf(create it if it doesn't exist).
**Here is a Wireshark Analysis of bgplu.cap**
![[bgplu_analysis.png]]


2. Install snort using docker:
```bash
docker run --name snort3 -v /volume:~/volume -h snort3 -u snorty -w /home/snorty -d -it ciscotalos/snort3 bash
```
This will download the snort image from docker hub and run a container with hostname as snort3 and user as snorty.
```bash
docker exec -it snort3 bash
```
Just with these 2 commands, you will have a interactive bash shell of a container with snort installed in it.

3. Now type the following commands:
```bash
cd
mkdir test && cd test
cp ../volume/bgplu.cap .
touch local.rules
```
now we have a local.rules file, in which we are going to write our snort rules

4. Edit the local.rules file
```bash
vim local.rules
```
Snort Rule:
```r
alert tcp 10.1.1.1 any -> 10.1.1.2 any (msg:"Lol, you are compromised, TCP detected from 10.1.1.1 to 10.1.1.2"; sid:1000001;)
```
Enter this rule in the local.rules file

5. Lastly run the following command
```bash
snort -q --talos -r bgplu.cap -R local.rules
```
You should see a result like this

![[snort_rule_output.png]]
We just alerted our user for tcp packets coming from 10.1.1.1 to 10.1.1.2,
* The rule applies for any port, in case you want to be port specific, just replace any from the snort rule to port number, for example `10.1.1.1 any -> 10.1.1.2 80`\
* Rule Action -> alert
This is just a demo of what we can achieve using snort, with complex rules, we can effectively prevent attackers from ever even reaching the systems of users, let alone
affecting them. **Snort not only detects but also prevents.**



**Resources**:
https://packetlife.net/captures/protocol/tcp/
https://docs.snort.org/start/rules
https://hub.docker.com/r/ciscotalos/snort3