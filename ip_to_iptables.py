#!/bin/env python3

import os

IP_FILE = "ips.txt"
RULES_FILE = "rules.txt"

try:
        with open(IP_FILE) as i:
                ips = i.readlines()
                ips = [ip.strip() for ip in ips]
except FileNotFoundError:
        print("IP file %s not found" % (IP_FILE))
        quit()

try:
        with open(RULES_FILE) as r:
                rules = r.readlines()
                rules = [rule.strip() for rule in rules]
except FileNotFoundError:
        rules = []

for i in ips:
        rule = "iptables -I INPUT -s %s/24 -j DROP" % (i)
        if rule not in rules:
                rules.append(rule)

with open(RULES_FILE, 'w') as r:
        for rule in rules:
                r.write("%s\n" % (rule))
