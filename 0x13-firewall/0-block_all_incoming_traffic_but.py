#!/usr/bin/env python3
# This script installs the ufw firewall and setup a few rules on web-01, web-02, lb-01

from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['54.236.30.33', '52.91.132.222', '54.236.45.24']
env.key_filename = '~/.ssh/school'

def ufw_setup():
    """Installs ufw and sets up the rules"""
    run("sudo ufw enable")
    run("sudo ufw allow 22/tcp") # SSH
    run("sudo ufw allow 443/tcp") # HTTPS/SSL
    run("sudo ufw allow 80/tcp") # HTTP
    run("sudo ufw status")


