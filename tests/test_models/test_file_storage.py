#!/usr/bin/python3
# test_file_storage.py
"""A module for unittesting the file_storage module comtaining
            the class FileStorage
"""

from models.engine.file_storage import FileStorage
import unittest, json, os, models


class TestFileStorageInstances(unittest.TestCase):
    """class for unittesting FileStorage private class attributes"""
    def test_file_storage_type(self):

        self.assertEqual(FileStorage, type(FileStorage()))

    def test_no_args(self):
        self.assertTrue(FileStorage())

    def test_private_file_path(self):
        with self.assertRaises(AttributeError) as f:
            FileStorage().__file_path

    def test_private_objects(self):
        with self.assertRaises(AttributeError) as f:
            FileStorage().__file_path

    def test_args(self):
        with self.assertRaises(TypeError) as f:
            FileStorage("Hello")

class TestAllMetod(unittest.TestCase):
    pass
