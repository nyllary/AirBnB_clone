#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_state_instance_creation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attribute_assignment(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_state_str_representation(self):
        state = State()
        state.name = "California"

        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()
