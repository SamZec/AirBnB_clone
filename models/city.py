#!/usr/bin/python3
# city.py
"""a module containing the class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        a class that defines a city inheriting from BaseModel.

        class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string

    """
    state_id = ''
    name = ''
