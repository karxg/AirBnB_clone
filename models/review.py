#!/usr/bin/python3
"""a class that inherets"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherts"""

    place_id = ""
    user_id = ""
    text = ""
