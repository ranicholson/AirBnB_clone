#!/usr/bin/python3

"""serializes instances to a JSON file and deserialize JSON file to instances"""

import json
from models.base import BaseModel


class FileStorage:
    """File storage class that serializes and deserializes to and from  JSON
    Class Attributes:
        file_path - path to JSON file
        objects - dictionary used to store objects by ID
    """

    __file_path = file.json
    __objects = {}

    def __init__(self):
        """Instantation method"""
        pass

    def all(self):
        """Returns dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """sets object into __objects with id key pairing.
        """
        objects['self.__class__.id'] = self.id

    def save(self):
        """Serialize objects to JSON file
        """
        with open(__file_path, "w") as file:
                json.dump(__objects, file)

    def reload(self):
        """Deserialize from JSON file
        """
        with open(__file_path, "r") as file:
            __objects = json.load(file)
