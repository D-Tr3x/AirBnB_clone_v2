#!/usr/bin/python3
"""
Fabfile based on `2-do_deploy_web_static.py` that creates and distributes
an archive to the web servers, using the function `do_deploy`
"""
from datetime import datetime
from fabric.api import env, local, put, run
import os
from os.path import basename


env.hosts = ['18.235.234.179', '54.160.94.251']
env.user = 'ubuntu'
env.key_filename = ['/home/d_trex/.ssh/id_rsa']


def do_pack():
    """ Generates a .tgz archive of the web_static folder """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{timestamp}.tgz'

    if not os.path.exists('versions'):
        os.makedirs('versions')
    if local(f'tar -czf {archive_path} web_static').failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """ Distributes an archive to the web server

    Returns:
        False if the file at the path `archive_path` doesn't exist
    """
    if not os.path.exists(archive_path):
        return False
    filename = basename(archive_path)
    folder_name = filename.split('.')[0]

    try:
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{folder_name}/')
        main_location = f'/data/web_static/releases/{folder_name}'
        run(f'tar -xzf /tmp/{filename} -C {main_location}/')
        run(f'rm /tmp/{filename}')
        run(f'mv {main_location}/web_static/* {main_location}/')
        run(f'rm -rf {main_location}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {main_location} /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to the web servers,
        by calling do_pack() and do_deploy(archive_path)

    Returns:
        False if no archive has been created.
        Otherwise, returns the value of do_deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
