#!/usr/bin/python3
"""This module instantiates a storage object"""
import os


store_type = os.getenv('HBNB_TYPE_STORAGE')

if store_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
