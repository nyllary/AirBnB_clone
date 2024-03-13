#!/usr/bin/python3
"""This test for the cases the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This houses all the tests for the BaseModel"""
    def test_ifnotempty(self):
        """Tests if an argument is passed"""
        with self.assertRaises(TypeError):
            test_instance = BaseModel(4)
            print(base)

    def test_forInstance(self):
        """"Tests if the BaseModel is an instance"""
        test_instance = BaseModel()
        self.assertIsInstance(test_instance, BaseModel)


if __name__ == "__main__":
    unittest.main()
