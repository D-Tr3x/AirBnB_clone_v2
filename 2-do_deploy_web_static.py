#!/usr/bin/python3
"""
Fabfile based on thr file `1-pack_web_static.py` that distributes an archive
to the web servers, using the function `do_deploy`
"""
from fabric.api import env, put, run
import os
from os.path import basename


env.hosts = ['18.235.234.179', '54.160.94.251']
env.user = 'ubuntu'
env.key_filename = ['/home/d_trex/.ssh/id_rsa']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers

    Returns:
        False if the file at the path `archive_path` doesn't exist
        otherwise, True
    """
    if not os.path.exists(archive_path):
        return False

    filename = basename(archive_path)
    folder_name = filename.split('.')[0]

    try:
        put(archive_path, f'/tmp/{filename}')

        run(f'rm -rf /data/web_static/releases/{folder_name}')

        run(f'mkdir -p /data/web_static/releases/{folder_name}/')
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename, folder_name))

        run(f'rm /tmp/{filename}')
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(folder_name, folder_name))

        run(f'rm -rf /data/web_static/releases/{folder_name}/web_static')


        run(f'rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(folder_name))
        return True
    except Exception as e:
        return False
