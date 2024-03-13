#!/usr/bin/python3
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        user = User()
        self.storage.new(user)
        self.assertIn('User.' + user.id, self.storage.all())

    def test_save_reload(self):
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()
        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('User.' + user.id, new_storage.all())
        self.assertIn('Place.' + place.id, new_storage.all())
        self.assertIn('State.' + state.id, new_storage.all())
        self.assertIn('City.' + city.id, new_storage.all())
        self.assertIn('Amenity.' + amenity.id, new_storage.all())
        self.assertIn('Review.' + review.id, new_storage.all())


if __name__ == '__main__':
    unittest.main()
