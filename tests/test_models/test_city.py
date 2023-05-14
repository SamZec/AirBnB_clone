#!/usr/bin/python3
# test_city.py
"""A module for unittesting city module contaning City class"""

from models.base_model import BaseModel
from models.city import City
from datetime import datetime
import unittest


class TestCityIntance(unittest.TestCase):
    """A class for unittesting City instance"""
    def test_city_type(self):
        self.assertTrue(type(City), BaseModel)

    def test_city_state_id_type(self):
        self.assertEqual(type(City().state_id), str)

    def test_city_name_type(self):
        self.assertEqual(type(City().name), str)

    def test_city_id(self):
        self.assertTrue(City().id)

    def test_city_created_at(self):
        self.assertTrue(City().created_at)

    def test_city_updated_at(self):
        self.assertTrue(City().updated_at)


class TestCreateCity(unittest.TestCase):
    """A class for unittesting City instance creation"""
    def test_no_arg(self):
        c = City()

        self.assertTrue(type(c), City)

    def test_unsed_args(self):
        c = City('Accra', 5)

        self.assertNotIn('Accra', c.__dict__)

    def test_kwargs(self):
        c = City(name='Tema')

        self.assertEqual(c.name, 'Tema')

    def test_creat_from_dict(self):
        _dict = {'name': 'Tema', 'state_id': 5}
        c = City(**_dict)

        self.assertEqual(c.name, 'Tema')
        self.assertEqual(c.state_id, 5)

    def test_unique_id(self):
        c1 = City()
        c2 = City()

        self.assertNotEqual(c1.id, c2.id)

    def test_created_at_type(self):
        self.assertEqual(type(City().created_at), datetime)

    def test_update_at_type(self):
        self.assertEqual(type(City().updated_at), datetime)

    def test_print_instance(self):
        c = City()
        _str = '[{}] ({}) {}'.format(c.__class__.__name__, c.id, c.__dict__)

        self.assertEqual(_str, str(c))

    def test_save_method(self):
        c1 = City()
        update_at = c1.updated_at
        c1.save()

        self.assertNotEqual(update_at, c1.updated_at)


class TestCityToDict(unittest.TestCase):
    """A class for unittesting city inherited method to_dict"""
    def test_inst_to_dict_type(self):
        c = City().to_dict()

        self.assertEqual(type(c), dict)

    def test_class_name_in_dict(self):
        c = City().to_dict()

        self.assertTrue(c['__class__'] == 'City')

    def test_created_at_str(self):
        c = City().to_dict()

        self.assertEqual(type(c['created_at']), str)

    def test_created_at_datetime_format(self):
        c = City()
        _dict = c.to_dict()

        self.assertEqual(_dict['created_at'], c.created_at.isoformat())

    def test_updated_at_str(self):
        c = City().to_dict()

        self.assertEqual(type(c['updated_at']), str)

    def test_updated_at_datetime_format(self):
        c = City()
        _dict = c.to_dict()

        self.assertEqual(_dict['updated_at'], c.updated_at.isoformat())
