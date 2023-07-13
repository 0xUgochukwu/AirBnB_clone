#!/usr/bin/python3
""" File Storage Module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage Class """
    __file_path = 'database.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        dict_objects = {}
        for key in self.__objects:
            dict_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(dict_objects, json_file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as json_file:
                data = json.load(json_file)
                for key, args in data.items():
                    self.__objects[key] = globals()[args['__class__']](**args)
        except Exception as e:
            pass
