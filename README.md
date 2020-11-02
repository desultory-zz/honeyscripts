# honeyscripts
scripts to deal with honeypots


# files
- log_to_ip.py

reads a ssh honeypot log file and writes all ips to a file, keeps history and deduplicates

- ip_to_iptables.py

reads ip file and creates iptables rules to block all ips in the file
the file created is effectively a bash script
