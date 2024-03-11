#!/usr/bin/python3
"""This houses the information on the amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This houses the amenities information"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the constructor method"""
        super().__init__(*args, **kwargs)
