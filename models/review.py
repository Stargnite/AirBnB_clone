#!/usr/bin/python3
"""Define reveiw class from BaseModel"""
from model.base_models import BaseModel

    
    class Review(BaseModel):
    
     """Represent a Review.
     
       Attrivutes:
       place_id(str) The usr place id.
       user_id(str) The usr id.
       text(str) The text of Review or commet.
       """
       
    place_id = ""
    user_id = ""
    text = ""
