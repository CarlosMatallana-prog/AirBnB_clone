#!/usr/bin/python3
""" base_model.py  """
import models
import uuid
from datetime import datetime


class BaseModel:
    """Defines the base model."""

    def __init__(self, *args, **kwargs):
        """ init method """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns info about class."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Assigns with the current datetime when an instance is created and
        it will be updated every time the object is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
