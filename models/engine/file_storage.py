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
         
