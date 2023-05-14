#!/usr/bin/python3
# review.py
"""a module that contains the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        a class that defines review inheriting from BaseModel

        class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string

    """
    place_id = ''
    user_id = ''
    text = ''
