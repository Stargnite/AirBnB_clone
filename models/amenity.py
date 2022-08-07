#!/usr/bin/python3
"""Difining amenity in BaseModel"""

from model.base_models import BaseModel

   class Amenity(BaseModel)
       """Represente an emenity in BaseModel """
    
    name = ""
    
def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
