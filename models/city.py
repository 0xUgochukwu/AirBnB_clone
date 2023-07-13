#!/usr/bin/python3
"""City Module"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City Class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
