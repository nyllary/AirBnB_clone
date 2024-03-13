#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_amenity_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attribute_assignment(self):
        amenity = Amenity()
        amenity.name = "WiFi"

        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_str_representation(self):
        amenity = Amenity()
        amenity.name = "WiFi"

        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
