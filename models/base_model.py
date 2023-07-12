#!/usr/bin/python3
"""
BaseModel Class
"""
import uuid, datetime

class BaseModel:
	"""A BaseModel class"""

		def __init__(self):
	self.id = str(uuid.uuid4())
	self.created_at = datetime.now()
	self.updated_at = self.created_at



