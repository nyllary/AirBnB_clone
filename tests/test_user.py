#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def test_user_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assignment(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_user_str_representation(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

if __name__ == '__main__':
    unittest.main()
