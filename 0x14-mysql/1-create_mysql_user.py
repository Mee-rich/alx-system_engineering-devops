#!/usr/bin/env python3
# This fabfile creates user on both web-01 and web-02

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.236.30.33', '52.91.132.222']
env.key_filename = '~/.ssh/school'

#MySQL credentials
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Ade@123'
NEW_USER = 'holberton_user'
NEW_PASSWORD = 'projectcorrection280hbtn'


def create_mysql_user():
    """Creating a user"""
    with prefix(f"mysql -u {MYSQL_USER} -p'{MYSQL_PASSWORD}'"):
        sudo(f"mysql -e \"CREATE USER '{NEW_USER}'@'localhost' IDENTIFIED BY '{NEW_PASSWORD}';\"")
        sudo(f"mysql -e \"GRANT REPLICATION CLIENT ON *.* TO '{NEW_USER}'@'localhost';\"")
        sudo(f"mysql -e \"FLUSH PRIVILEGES;\"")
