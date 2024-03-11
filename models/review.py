#!/usr/bin/python3
"""This houses the reviews from users"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class captures the reviews"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This is the constructor method"""
        super().__init__(*args, **kwargs)
