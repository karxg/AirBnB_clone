#!/usr/bin/python3
"""Defines the Review class, a subclass of BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review made by a user for a place."""

    place_id = ""
    user_id = ""
    text = ""
