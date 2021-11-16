#!/usr/bin/python3

"""
Module for file storage for base models

"""

import json
from models.base_model import BaseModel
from os import path
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
import sys


class FileStorage:
    """ A class that helps to serializes to a JSON 
    and deserializes file to an instace of Basemodel
    and the user
    """
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """Initialization"""
        pass

    def all(self):
        """Returns dictionary object """
        return (self.__objects)

    def new(self, obj):
        """Helps to set in _obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "."+ obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        dic_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(dic_obj, f)

    def reload(self):
        """ Deseriliazes the JSON file to __object """
        fil = self.__file_path
        if path.isfile(fil):
            with open(FileStorage.__file_path, "r") as f:
               json_f =  json.load(f)
               for value in json_f.values():
                   clsName = value["__class__"]
                   del value["__class__"]
                   self.new(eval(clsName)(**value))
