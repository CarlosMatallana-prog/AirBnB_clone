#!/usr/bin/python3
""" Module for storing and reload from JSON file"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage():
    """ FileStorage Class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return dict objects """
        return self.__objects

    def new(self, obj):
        """ Creates a new instance of a object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Save content """
        dicto = {}
        for key, obj in self.__objects.items():
            dicto[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(dicto, f)

    def reload(self):
        """ Load JSON content of <file.json> """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    val = eval(key.split(".")[0])(**val)
                    FileStorage.__objects[key] = val
        except FileNotFoundError:
            pass

    def delete(self, class_name="", class_id=""):
        """ Deletes an instance """
        switch = False
        string = class_name + "." + class_id

        for obj_id, obj in self.__objects.items():
            if string == obj_id:
                self.__objects.pop(string)
                self.save()
                switch = True
                return True

        if switch is False:
            return False

    def update(self, obj_id, key, value):
        """ Updates our multi dict object """
        try:
            if key != "updated_at" and key != "created_at" and key != "id":
                switch = True

                str_attributes = ["name", "state_id", "city_id", "user_id",
                                  "description", "place_id", "text"]
                for name in str_attributes:
                    if key == name:
                        switch = True
                        value = str(value)
                        break

                int_attributes = ["number_rooms", "number_bathrooms",
                                  "max_guest", "price_by_night"]
                for name in int_attributes:
                    if key == name:
                        try:
                            switch = True
                            value = int(value)
                            break
                        except ValueError:
                            print("*** Dont be silly cannot cast "
                                  "<{}> to int ***".format(value))
                            switch = False

                float_attributes = ["latitude", "longitude"]
                for name in float_attributes:
                    if key == name:
                        try:
                            switch = True
                            value = float(value)
                            break
                        except ValueError:
                            print("*** Dont be silly cannot cast "
                                  "<{}> to float ***".format(value))
                            switch = False

                if switch is True:
                    setattr(self.__objects[obj_id], key, value)
                    self.save()
                    return True

        except KeyError:
            return False
