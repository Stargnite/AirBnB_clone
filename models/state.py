#!/user/bin/python3
"""Define a state from BaseModel."""
from modeles.base_models import BaseModel


    class State(BaseModes):
       """Represent a state inherit from BaseModes"""
         
    name = ""
    
    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
