#!/usr/bin/python3
# fabric script to archive and deploy web_staic to web servers

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.229.186.107', '100.25.142.198']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """function compresses the target web_static"""

    file = datetime.now().strf('%Y%M%D%H%M%S')
    if local("mkdir -p versions").failed is True:
        return False

    if local("tar -czvf versions/web_static_{}.tgz /web_static/".format(file)).failed is True:
        return False

    return 'versions/web_static_{}.tgz'.format(file)


def do_deploy(archive_path)
    """function deploys the archive to the servers"""

    if path.isfile(archive_path) is False:
        return False

