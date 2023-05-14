#!/usr/bin/python3
# test_user.py
"""A module for unittesting user.py module containing User class"""

from models.base_model import BaseModel
from models.user import User
import models
import json
import unittest


class TestUserInstances(unittest.TestCase):
    """A class for unittesting User instances"""
    def test_user_type(self):
        self.assertTrue(type(User), BaseModel)

    def test_no_args(self):
        self.assertTrue(User())

    def test_email_attribute(self):
        self.assertEqual(type(User.email), str)

    def test_password_attribute(self):
        self.assertTrue(type(User.password), str)

    def test_first_name_attribute(self):
        self.assertEqual(type(User.first_name), str)

    def test_last_name_attribute(self):
        self.assertEqual(type(User.last_name), str)
