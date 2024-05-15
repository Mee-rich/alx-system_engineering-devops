#!/usr/bin/env python3
# This script installs mysql on the web-01 and web-02 servers

from fabric.api import *
import time
env.user = 'ubuntu'
env.hosts = ['54.236.30.33', '52.91.132.222']
env.key_filename = '~/.ssh/school'

def install():
    """Installation of MySQL"""
    sudo('wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57')
    sudo('chmod +x mysql57')
    time.sleep(15)
    sudo('./mysql57')
