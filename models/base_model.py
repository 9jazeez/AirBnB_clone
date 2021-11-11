#!/usr/bin/python3

"""
This module contains the base model for all other classes
It contains common attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """The base model with the following public instances

    id, created_at and updated_at.
    """
    def __init__(self, *args, **kwargs):
        """Base class initialisation"""

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v,"%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str rep of class"""
        clsName = self.__class__.__name__
        val = "[" + clsName + "] " + "(" + self.id + ") " + str(self.__dict__)
        return (val)

    def save(self):
        """Updates the public instance with updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """First level of serialization/deserialization for the base model"""
        dic = dict()
        d1 = datetime.now()
        for k, v in vars(self).items():
            if type(v) == type(d1):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        dic["__class__"] = self.__class__.__name__

        return (dic)
