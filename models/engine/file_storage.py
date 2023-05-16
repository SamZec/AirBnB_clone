#!/usr/bin/python3
# file_storage.py
"""a module that contains FileStorage class for JSON serialization and
    deserialization to and from a file
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
     serializes instances to a JSON file and deserializes
     JSON file to instances

     Private class attributes:
     __file_path -  string - path to the JSON file (ex: file.json)
     __objects - dictionary - empty but will store all objects
                by <class name>.id

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objs = FileStorage.__objects
        obj_dict = {obj: objs[obj].to_dict() for obj in objs.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dicts = json.load(f)
                for obj in obj_dicts.values():
                    obj_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(obj_name)(**obj))
        except FileNotFoundError:
            return
