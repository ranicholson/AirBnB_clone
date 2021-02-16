#!/usr/bin/python3

"""serializes instances to a JSON file > deserialize JSON file to instances"""

import models
import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage class that serializes and deserializes to and from  JSON
    Class Attributes:
        file_path - path to JSON file
        objects - dictionary used to store objects by ID
    """

    __file_path = "file.json"
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
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)]\
            = obj

    def save(self):
        """Serialize objects to JSON file
        """
        ndict = {}
        for key, value in FileStorage.__objects.items():
            ndict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
                json.dump(ndict, file)

    def reload(self):
        """Deserialize from JSON file
        """
        if os.path.isfile(self.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                temp = json.load(file)
                for key, value in temp.items():
                    clrel = temp[key]["__class__"]
                    gclass = models.cdict[clrel]
                    self.__objects[key] = gclass(**value)
