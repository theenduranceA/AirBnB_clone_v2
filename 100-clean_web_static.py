#!/usr/bin/python3
"""
Script that deletes out-of-date archives,
using the function do_clean.
"""
import os.path
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
import time
env.hosts = ["35.174.205.224", "54.172.243.100"]


def do_pack():
    """Module for do_pack"""

    tell_time = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(tell_time))
        return ("versions/web_static_{}.tgz".format(tell_time))
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ Module for do_deploy function."""

    if os.path.isfile(archive_path) is False:
        return False

    test1 = archive_path.split('/')[1].split('.')[0]
    test2 = archive_path.split('/')[1]

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(test1))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/ \
                releases/{}/".format(test2, test1))
        run("sudo rm /tmp/{}".format(test2))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(test1, test1))
        run("sudo rm -rf /data/web_static/releases/{} \
                /web_static".format(test1))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(test1))

        return True

    except Exception:

        return False


def deploy():
    """ Module for deploy function"""

    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    """ Module for do_clean function."""

    if number == 0 or number == 1:
        with cd.local('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +1 | xargs -d '\n' rm -rf")
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +1 | xargs -d '\n' rm -rf")
    else:
        with cd.local('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +{} | xargs -d '\n' rm -rf".format(number))
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +{} | xargs -d '\n' rm -rf".format(number))
