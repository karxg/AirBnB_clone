#!/usr/bin/python3
"""
class BaseModel that defines all common
attributes/methods for other classes:
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all
    common attributes/methods for other classes:
    """
    def __init__(self):
        """_summary_

        Args:
              x (_type_): _description_
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[<{self.__class__.__name__}>] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
