#!/usr/bin/python3
# state.py
"""a module that contains class state"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        a class that difines a state inherinting from BaseModel

        class attribute:
        name: string-empty
    """
    name = ''
