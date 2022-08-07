#!/user/bin/python3
"""Defines the user in BaseModel"""
from models.base_models import BaseModel


class User(BaseModel)
      """ class User."""
    
       email = ""
       password = ""
       fist_name = ""
       last_name = ""
  
def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
