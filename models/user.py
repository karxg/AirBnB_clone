#!/usr/bin/python3
"""Defines the User class, a subclass of BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user of the system."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
