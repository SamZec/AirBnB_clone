#!/usr/bin/pytohn3
# test_base_model.py
"""A module for unittesting base_model module containing class BaseModel"""

from models.base_model import BaseModel
import json
import unittest
import sys
import os
from datetime import datetime
import models


class TestBaseModelInstance(unittest.TestCase):
    """Class for testing BaseModel public Instance attributes"""
    def test_for_instance(self):
        base = BaseModel()

        self.assertIsInstance(base, BaseModel)

    def test_instance_id(self):
        base = BaseModel()

        self.assertEqual(str, type(base.id))

    def test_unique_id(self):
        base = BaseModel()
        base2 = BaseModel()

        self.assertNotEqual(base.id, base2.id)

    def test_assigned_1_attributes(self):
        base = BaseModel()
        base.number = 1

        self.assertEqual(base.number, 1)

    def test_assigned_multiple_attributes(self):
        base = BaseModel()
        base.number = 2
        base.name = "Affum"
        base.city = "Accra"

        self.assertTrue(base.number)
        self.assertTrue(base.name)
        self.assertTrue(base.city)

    def test_created_at_type(self):
        base = BaseModel()

        self.assertIsInstance(base.created_at, datetime)

    def test_updated_at_type(self):
        base = BaseModel()

        self.assertIsInstance(base.updated_at, datetime)

    def test_print_instance(self):
        base = BaseModel()
        _str = base.__str__()
        _str_output = '[{}] ({}) {}'.format(
                base.__class__.__name__, base.id, base.__dict__)

        self.assertEqual(_str, _str_output)

    def test_save_method(self):
        base = BaseModel()
        base.save()

        self.assertNotEqual(base.created_at, base.updated_at)

    def test_dict_method(self):
        base = BaseModel()

        self.assertEqual(type(base.to_dict()), dict)


class TestBaseModelArgsKwargs(unittest.TestCase):
    """class for unttesting *args and **kwargs passed to BaseModel"""
    def test_no_args(self):
        base = BaseModel()

        self.assertTrue(base)

    def test_one_arg(self):
        with self.assertRaises(AttributeError) as f:
            base = BaseModel("name")
            self.assertEqual(base.name, f)

    def test_multiple_args(self):
        with self.assertRaises(AttributeError) as f:
            base = BaseModel("name", "my_number",)
            base.my_number

            self.assertTrue(f)

    def test_one_kwarg(self):
        base = BaseModel(name="My_first_model")

        self.assertTrue(base.name)

    def test_multiple_kwargs(self):
        base = BaseModel(name="My_first_model", my_number=10)

        self.assertTrue(base.name)
        self.assertTrue(base.my_number)

    def test_dict_to_instace(self):
        base = BaseModel(name="My_First_Model", my_number=89)
        _dict = base.to_dict()
        new_base = BaseModel(**_dict)

        self.assertNotEqual(base, new_base)

    def test_empty_dict_to_instance(self):
        _dict = {}
        base = BaseModel(**_dict)

        self.assertTrue(base)

    def test_to_dict_none(self):
        with self.assertRaises(TypeError) as f:
            BaseModel().to_dict(t=1)
