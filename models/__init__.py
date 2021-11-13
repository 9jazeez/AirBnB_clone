#!/usr/bin/python3

"""
This module is used to create a unique Filestorage instance

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
