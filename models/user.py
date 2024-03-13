#!/usr/bin/python3
"""This clas inherits from the BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class captures the user attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """This is the constructor method"""
        super().__init__(*args, **kwargs)
