#!/usr/bin/python3
""" File Storage Module """
import json

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
                json_object = json.load(json_file)
                #ERROR
                for key in json_object:
                    self.__objects[key] = globals()[json_object[key]['__class__']](**json_object[key])
        except:
            pass
