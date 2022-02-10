#!/usr/bin/python3
"""first class"""

import json


class Base():
    """first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs  to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string([
                    element.to_dictionary() for element in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(9, 8)
        if cls.__name__ == "Square":
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                to_read = myfile.read()
                lists_dic = cls.from_json_string(to_read)
                lists = []
                for k in lists_dic:
                    lists.append(cls.create(**k))
                return lists
        except Exception:
            return []
