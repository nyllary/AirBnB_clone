#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def test_review_instance_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assignment(self):
        review = Review()
        review.place_id = "1234"
        review.user_id = "5678"
        review.text = "This is a test review"

        self.assertEqual(review.place_id, "1234")
        self.assertEqual(review.user_id, "5678")
        self.assertEqual(review.text, "This is a test review")

    def test_review_to_dict(self):
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_review_str_representation(self):
        review = Review()
        review.text = "This is a test review"

        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)


if __name__ == '__main__':
    unittest.main()
