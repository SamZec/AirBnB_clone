#!/usr/bin/python3
# amenity.py
"""a module that contains the class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        a class that defines amenity inheriting from BaseModel.

        class attribute:
        name: string - empty string
    """
    name = ''
