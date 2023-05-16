#!/usr/bin/python3
# user.py
"""a module thta contains class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        a class that defines a user inheriting from BaseModel

        class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
