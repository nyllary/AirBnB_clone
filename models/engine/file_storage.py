#!/usr/bin/python3
"""This class serializes instances to a JSON file and
deserializes JSON file to instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """This method sets a new key and value to the
        __objects attribute
        Args:
            obj: The object to be stored in __objects
        Returns:
            None"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON
        file
        Args:
            None
        Returns:
            None"""
        total_objs = self.__objects
        local_dict = {}
        for obj_key, obj_instance in total_objs.items():
            local_dict[obj_key] = obj_instance.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as the_file:
            json.dump(local_dict, the_file)

    def reload(self):
        """This method deserializes the JSON file to
        __objects
        Args:
            None
        Returns:
            None"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as the_file:
                local_dict = json.load(the_file)
                for key, value in local_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    class_obj = BaseModel if class_name == 'BaseModel' else User
                    instance = cls(**value)
                    self.__objects[key] = instance
        else:
            pass
