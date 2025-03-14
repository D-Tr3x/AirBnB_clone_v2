#!/usr/bin/python3
"""This module instantiates an object of the storage engine

   If the environmental variable HBNB_TYPE_STORAGE is equal to "db",
   instantiate the DBStorage engine.
   Otherwise, instantiate the FileStorage engine.
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
