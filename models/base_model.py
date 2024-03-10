#!/usr/bin/python3
"""
BaseModel class that serves as the base for other classes.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            **kwargs: Key-value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the instance and updates the 'updated_at' attribute.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
