#!/usr/bin/python3
"""This is the class that defines all common attributes/methods
for other classes"""
import uuid
import json
from datetime import datetime


class BaseModel:
    """This is the base model for the airbnb project"""
    def __init__(self, *args, **kwargs):
        """
        This method initializes the instance of the class
        Args:
            None
        """
        import models
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    try:
                        setattr(self, key, datetime.strptime(
                            value, date_format))
                    except ValueError:
                        print("Invalid date format for {}: {}".format(
                            key, value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method prints the human readable format of
         the class """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance updated_at with
        current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary of the __dict__
        of the instance"""
        a = self.__dict__.copy()
        a['__class__'] = self.__class__.__name__
        a['created_at'] = a['created_at'].isoformat()
        a['updated_at'] = a['updated_at'].isoformat()
        return a
