#!/bin/env python3

import os
import ipaddress


LOG_DIR = "/var/log/"
LOG_FILE = "ssh-honeypot.log"
LOG_LOCATION = LOG_DIR + LOG_FILE
IP_FILE = "ips.txt"

allowed_ranges = [
        '172.16.0.0/16',
        '192.168.0.0/24',
        '10.0.0.0/8'
        ]

try:
        with open(IP_FILE) as i:
                ips = i.readlines()
                ips = [ip.strip() for ip in ips]
except FileNotFoundError:
        ips = []

try:
        with open(LOG_LOCATION) as l:
                log_data = (l.readlines())
                read_ips = [line.rsplit('] ')[1].rsplit(' ')[0] for line in log_data]
except FileNotFoundError:
        print("Log file %s not found" % (LOG_LOCATION))
        quit()

def check_ip(ip_address):
        if not ip_address[0].isnumeric():
                return False
        for net in allowed_ranges:
                try:
                        if ipaddress.IPv4Address(ip_address) in ipaddress.IPv4Network(net):
                                return False
                except ipaddress.AddressValueError:
                        pass
        if ip_address in ips:
                return False
        return True

for i in read_ips:
        if check_ip(i):
                ips.append(i)

with open(IP_FILE, 'w') as i:
        for ip in ips:
                i.write("%s\n" % (ip))
