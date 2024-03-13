#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_assignment(self):
        city = City()
        city.state_id = "1234"
        city.name = "New York"

        self.assertEqual(city.state_id, "1234")
        self.assertEqual(city.name, "New York")

    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_city_str_representation(self):
        city = City()
        city.name = "New York"

        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
