#!/usr/bin/python3

"""BaseModel Class"""
import uuid
import datetime


class BaseModel:
    """A BaseModel class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data[created_at] = self.created_at.isoformat()
        data[updated_at] = self.updated_at.isoformat()
        return data
