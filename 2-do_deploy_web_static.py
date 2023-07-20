#!/usr/bin/python3
""" script distributes an archive to your web servers """

import os
from fabric.api import *
from datetime import datetime


env.hosts = ['100.25.142.198', '54.237.15.47']
env.user = 'ubuntu'
env.key_filename = 'private'


def do_deploy(archive_path):
    """ function which uncompresses the archive """

    try:
        if not os.path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')

        timestamp = archive_path[-18, -4]
        run("sudo mkdir -p /data/web_static/releases/web_static_{}".format(
            timestamp))

        # uncompress the archive
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/\
releases/web_static_{}/".format(timestamp, timestamp))
        run("sudo mv /data/web_static/releases/web_static_{}/web_static/*\
/data/web_static/releases/web_static_{}/".format(timestamp, timestamp))

        run("sudo rm -rf /data/web_static/releases/web_static_{}/web_static")
        run("sudo rm /tmp/web_static_{}.tgz".format(timestamp))

        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))

    except Exception as e:
        return False

    return True
