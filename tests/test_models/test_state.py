#!/usr/bin/python3
# test_state.py
"""A module for unittesting state.py module containing class State"""

from models.base_model import BaseModel
from models.state import State
from datetime import datetime
import unittest


class TestStateIntance(unittest.TestCase):
    """Class for unittesting instance of State class"""
    def test_type_state(self):
        self.assertTrue(type(State), BaseModel)

    def test_state_instance_id(self):
        self.assertTrue(State().id)

    def test_name_attribute_empty(self):
        self.assertFalse(State.name)

    def test_type_name_attribute(self):
        self.assertEqual(type(State.name), str)

    def test_created_at(self):
        self.assertTrue(State().created_at)

    def test_updated_at(self):
        self.assertTrue(State().updated_at)

    def test_str_print_instance(self):
        self.assertEqual(type(State().__str__()), str)

    def test_print_instance(self):
        s = State()
        _str = '[{}] ({}) {}'.format(s.__class__.__name__, s.id, s.__dict__)

        self.assertEqual(_str, str(s))


class TestCreateState(unittest.TestCase):
    """A class for unittesting creation of State instances"""
    def test_no_args(self):
        s = State()

        self.assertIsInstance(s, State)

    def test_unsed_args(self):
        with self.assertRaises(AttributeError) as f:
            s = State("Greater_Acrra")
            s.Greater_Acrra

    def test_used_kwargs(self):
        s = State(name='Accra')

        self.assertEqual(s.name, 'Accra')

    def test_unique_id(self):
        s = State()
        s1 = State()

        self.assertNotEqual(s1.id, s.id)

    def test_created_time(self):
        s = State()

        self.assertEqual(type(s.created_at), datetime)

    def test_save_method(self):
        s = State()
        s.save()

        self.assertNotEqual(s.created_at, s.updated_at)

    def test_create_from_dict(self):
        _dict = {'name': 'Accra'}
        s = State(**_dict)

        self.assertEqual(s.name, 'Accra')


class TestStateToDict(unittest.TestCase):
    """A class for unittesting State inherited method to_dict()"""
    def test_dict_instance(self):
        self.assertEqual(type(State().to_dict()), dict)

    def test_class_name_in_dict(self):
        s = State().to_dict()

        self.assertEqual(s['__class__'], 'State')

    def test_creaed_at_str(self):
        s = State().to_dict()

        self.assertEqual(type(s['created_at']), str)

    def test_created_at_datetime_format(self):
        s = State()
        s1 = s.to_dict()

        self.assertEqual(s1['created_at'], s.created_at.isoformat())

    def test_update_at_str(self):
        s = State().to_dict()

        self.assertEqual(type(s['updated_at']), str)

    def test_updated_at_datetime_format(self):
        s = State()
        s1 = s.to_dict()

        self.assertEqual(s1['updated_at'], s.updated_at.isoformat())
