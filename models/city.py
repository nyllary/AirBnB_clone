#!/usr/bin/python3
"""This class houses the information on the city"""
from models.base_model import BaseModel


class City(BaseModel):
    """This houses the information on the city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the constructor method"""
        super().__init__(*args, **kwargs)
