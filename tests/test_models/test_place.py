#!/usr/bin/python3
# test_place.py
"""A module for unittesting place.py module containing class Place"""

from models.base_model import BaseModel
from models.place import Place
from datetime import datetime
import models
import unittest


class TestPlaceInstance(unittest.TestCase):
    """A class for unittesting Place instances"""
    def test_place_type(self):
        self.assertTrue(type(Place), BaseModel)

    def test_city_id(self):
        self.assertTrue(type(Place.city_id), str)

    def test_user_id(self):
        self.assertTrue(type(Place.user_id), str)

    def test_name(self):
        self.assertTrue(type(Place.name), str)

    def test_description(self):
        self.assertTrue(type(Place.description), str)

    def test_number_rooms(self):
        self.assertTrue(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        self.assertTrue(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        self.assertTrue(type(Place.max_guest), int)

    def test_price_by_night(self):
        self.assertTrue(type(Place.price_by_night), int)

    def test_latitude(self):
        self.assertTrue(type(Place.latitude), float)

    def test_longitude(self):
        self.assertTrue(type(Place.longitude), float)

    def test_amenity_ids(self):
        self.assertTrue(type(Place.amenity_ids), float)

    def test_created_at(self):
        self.assertTrue(Place().created_at)

    def test_updated_at(self):
        self.assertTrue(Place().updated_at)

    def test_place_id(self):
        self.assertTrue(Place().id)

    def test_string_instance(self):
        p = Place()

        self.assertEqual(str(p), p.__str__())

class TestCreatePlace(unittest.TestCase):
    """class for unittesting creation of Place instances"""
    def test_created_place_instance(self):
        p = Place()

        self.assertIsInstance(p, Place)

    def test_unique_id(self):
        p = Place()
        p1 = Place()

        self.assertNotEqual(p.id, p1.id)

    def test_create_time(self):
        p = Place()

        self.assertEqual(type(p.created_at), datetime)

    def test_updated_at(self):
        p = Place()

        self.assertEqual(type(p.updated_at), datetime)

    def test_create_time_not_update(self):
        p = Place()
        p.save()

        self.assertNotEqual(p.created_at, p.updated_at)

    def test_print_instance_format(self):
        p = Place()
        _str = '[{}] ({}) {}'.format(p.__class__.__name__, p.id, p.__dict__)
        
        self.assertEqual(_str, str(p))

    def test_args_unsed(self):
        with self.assertRaises(AttributeError) as f:
            p = Place("Accra")
            p.Accra

    def test_used_kwargs(self):
        p = Place(name='Accra')

        self.assertEqual(p.name, 'Accra')

    def test_create_instance_from_dict(self):
        p = Place().to_dict()
        p1 = Place(**p)

        self.assertIsInstance(p1, Place)

class TestDictPlace(unittest.TestCase):
    """A class for unittesting inherited dict method from BaseModel"""
    def test_created_dict(self):
        p = Place().to_dict()

        self.assertEqual(type(p), dict)

    def test_class_name_in_dict(self):
        p = Place().to_dict()

        self.assertEqual(p['__class__'], 'Place')

    def test_created_at_str(self):
        p = Place().to_dict()

        self.assertEqual(type(p['created_at']), str)

    def test_created_at_str_isoformat(self):
        p = Place()
        _dict = p.to_dict()

        self.assertEqual(_dict['created_at'], p.created_at.isoformat())

    def test_updated_at_str(self):
        p = Place().to_dict()

        self.assertEqual(type(p['updated_at']), str)

    def test_updated_at_isoformat(self):
        p =Place()
        _dict = p.to_dict()

        self.assertEqual(_dict['updated_at'], p.updated_at.isoformat())
