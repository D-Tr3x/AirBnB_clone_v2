#!/usr/bin/python3
"""
Fabfile that generates a .tgz archive from the contents of web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder

    Returns:
        The archive path if the archive generation was successful,
        otherwise, returns None
    """
    if not os.path.exists('versions'):
        os.makedirs('versions')

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{timestamp}.tgz'

    result = local(f'tar -czvf {archive_path} web_static')
    if result.failed:
        return None

    return archive_path
