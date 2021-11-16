#!/usr/bin/python3

"""
This module is for creating and using a user class
in the AirBnB clone project

"""
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class User(BaseModel):
    """ This is a user class that inherits from the base class
    BaseModel
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
            BaseModel.__init__(self)
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
