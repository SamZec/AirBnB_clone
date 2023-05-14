#!/usr/bin/python3
# review.py
"""A module for unittesting review.py module containing class Review"""

from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
import unittest


class TestReviewInstanceType(unittest.TestCase):
    """A class for unittesting Review instances"""
    def test_review_type(self):
        self.assertTrue(type(Review), BaseModel)

    def test_no_args(self):
        r = Review()

        self.assertTrue(type(r), Review)

    def test_place_id_type(self):
        self.assertEqual(type(Review.place_id), str)

    def test_place_id_empty(self):
        self.assertFalse(Review.place_id)

    def test_user_id_type(self):
        self.assertEqual(type(Review.user_id), str)

    def test_user_id_empty(self):
        self.assertFalse(Review.user_id)

    def test_text_type(self):
        self.assertEqual(type(Review.text), str)

    def test_text_empty(self):
        self.assertFalse(Review.text)

    def test_unique_id(self):
        r1 = Review()
        r2 = Review()

        self.assertNotEqual(r1, r2)

    def test_created_at(self):
        r = Review()

        self.assertEqual(type(r.created_at), datetime)

    def test_update_at(self):
        r = Review()

        self.assertEqual(type(r.updated_at), datetime)

    def test_print_instance(self):
        r = Review()
        _str = '[{}] ({}) {}'.format(r.__class__.__name__, r.id, r.__dict__)

        self.assertEqual(_str, str(r))

class TestReviewToDictToInstance(unittest.TestCase):
    """A class for unittesting to_dict method of Review"""
    def test_to_dict_type(self):
        self.assertEqual(type(Review().to_dict()), dict)

    def test_class_name_in_dict(self):
        r = Review().to_dict()

        self.assertEqual(r['__class__'], 'Review')

    def test_create_from_dict(self):
        r1 = Review().to_dict()
        r2 = Review(**r1)

        self.assertNotEqual(r1, r2)
