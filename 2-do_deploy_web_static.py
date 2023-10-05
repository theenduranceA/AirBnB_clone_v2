#!/usr/bin/python3
"""
Script that that distributes an archive to my web servers,
using the function do_deploy.
"""
import os.path
from fabric.api import *
env.hosts = [
        '35.174.205.224',
        '54.172.243.100']


def do_deploy(archive_path):
    """ Module for deploy """

    if (os.path.isfile(archive_path) is False):
        return False

    try:
        test1 = archive_path.split("/")[-1]
        test2 = (
                "/data/web_static/releases/" + test1.split(".")[0]
                )

        put(archive_path, "/tmp/")
        run(
                "sudo mkdir -p {}".format(test2))
        run(
                "sudo tar -xzf /tmp/{} -C {}".format(test1, test2))
        run(
                "sudo rm /tmp/{}".format(test1))
        run(
                "sudo mv {}/web_static/* {}/".format(test2, test2))
        run(
                "sudo rm -rf {}/web_static".format(test2))
        run(
                'sudo rm -rf /data/web_static/current')
        run(
                "sudo ln -s {} /data/web_static/current".format(test2))
        return True

    except Exception:
        return False
