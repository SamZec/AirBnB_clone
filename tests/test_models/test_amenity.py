#!/usr/bin/python3
# test_amenity.py
"""A module for unittesting amenity.py containing Amenity class"""

from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
import unittest


class TestAmenityInstace(unittest.TestCase):
    """A class for testing Amenity instances"""
    def test_amenity_type(self):
        self.assertTrue(type(Amenity), BaseModel)

    def test_amenity_instance_id(self):
        self.assertTrue(Amenity().id)

    def test_amenity_created_at(self):
        self.assertTrue(Amenity().created_at)

    def test_amenity_updated_at(self):
        self.assertTrue(Amenity().updated_at)

    def test_amenity_name_type(self):
        self.assertEqual(type(Amenity.name), str)

    def test_amenity_name_empty(self):
        self.assertFalse(Amenity.name)

class TestCreateAmenityInstance(unittest.TestCase):
    """A class for uittesting Amenity instance creation"""
    def test_create_no_args(self):
        self.assertTrue(type(Amenity()), Amenity)

    def test_unsed_args(self):
        with self.assertRaises(AttributeError) as f:
            a = Amenity("Bed")
            a.Bed

    def test_used_kwargs(self):
        a = Amenity(bed='latex')
        
        self.assertEqual(a.bed, 'latex')

    def test_create_from_dict(self):
        _dict = {'name': 'bed', 'type': 'latex'}
        a = Amenity(**_dict)

        self.assertEqual(a.name, 'bed')
        self.assertEqual(a.type, 'latex')

    def test_created_at_not_updated_at(self):
        a = Amenity()

        self.assertNotEqual(a.created_at, a.updated_at)

    def test_print_instance(self):
        a = Amenity()
        _dict = '[{}] ({}) {}'.format(a.__class__.__name__, a.id, a.__dict__)

        self.assertEqual(_dict, str(a))

class TestAmenityToDict(unittest.TestCase):
    """A clsss for unittesting Amenity inherited method to_dict()"""
    def test_instance_to_dict_type(self):
        a = Amenity().to_dict()

        self.assertEqual(type(a), dict)

    def test_class_name_in_dict(self):
        a = Amenity().to_dict()

        self.assertEqual(a['__class__'], 'Amenity')

    def test_created_at_str(self):
        a = Amenity().to_dict()

        self.assertEqual(type(a['created_at']), str)

    def test_created_at_datetime_format(self):
        a = Amenity()
        a1 = a.to_dict()

        self.assertEqual(a1['created_at'], a.created_at.isoformat())

    def test_created_at_str(self):
        a = Amenity().to_dict()

        self.assertEqual(type(a['updated_at']), str)

    def test_created_at_datetime_format(self):
        a = Amenity()
        a1 = a.to_dict()

        self.assertEqual(a1['updated_at'], a.updated_at.isoformat())


