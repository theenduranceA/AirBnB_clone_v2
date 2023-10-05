#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of the
web_static folder of my AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import *
import time


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
