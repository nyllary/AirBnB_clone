#!/usr/bin/python3
"""create an instance of FileStorage by importing
then calling the reload method
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
