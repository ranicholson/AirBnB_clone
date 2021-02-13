#!/usr/bin/python3

"""serializes instances to a JSON file and deserialize JSON file to instances"""

import json
from models.base_model import BaseModel


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
            ndict = value.to_dict()
        with open(FileStorage.__file_path, "a") as file:
                file.write(json.dumps(ndict))

    def from_json_string(json_string):
        """ converts json strings into a list to represent objects """
        j_str = []
        if json_string is None or len(json_string) == 0:
            return j_str
        else:
            return json.loads(json_string)

    def reload(self):
        """Deserialize from JSON file
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                """ open and read the file where objs are stored """
                FileStorage.from_json_string(f.read())
        except:
            return
