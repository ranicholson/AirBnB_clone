#!/usr/bin/python3

"""Subclass Review that inherits from BaseModel"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Class Review subclass of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
