#!/usr/bin/python3
"""This class houses the information on the User State"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class houses the State name"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the constructor method"""
        super().__init__(*args, **kwargs)
