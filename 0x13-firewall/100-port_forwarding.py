#!/usr/bin/env python3
# This script performs port forwarding

from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['54.236.30.33', '52.91.132.222', '54.236.45.24']
env.key_filename = '~/.ssh/school'

def ufw_port_forwarding():
    # Check if *nat exists in the file
    nat_exists = sudo("grep -q '^\\*nat$' /etc/ufw/before.rules && echo 'true' || echo 'false'")

    if nat_exists == 'true':
        # If *nat exists, append the port forwarding rule after it
        sudo("sed -i '/^\\*nat$/a -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80' /etc/ufw/before.rules")
    else:
        # If *nat does not exist, append it along with the port forwarding rule
        sudo("echo '*nat' | sudo tee -a /etc/ufw/before.rules > /dev/null")
        sudo("echo '-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80' | sudo tee -a /etc/ufw/before.rules > /dev/null")
        sudo("echo 'COMMIT' | sudo tee -a /etc/ufw/before.rules > /dev/null")
    sudo("ufw reload")


