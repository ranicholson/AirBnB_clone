#!/usr/bin/python3

"""Importing storage variable"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

cdict = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
