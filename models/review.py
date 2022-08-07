 #!/usr/bin/python3
"""Define reveiw class from BaseModel"""
from models.base_model import BaseModel

    
    class Review(BaseModel):
     """Represent a Review or commet inherits from BaseModel"""
       
    place_id = ""
    user_id = ""
    text = ""  
