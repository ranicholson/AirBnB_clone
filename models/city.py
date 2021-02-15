#!/usr/bin/python3

"""City is subclass of BaseModel"""

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """City subclass of BaseModel"""

    state_id = ""
    name = ""
