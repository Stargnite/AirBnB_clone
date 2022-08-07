 #!/usr/bin/python3
"""Define reveiw class from BaseModel"""
from model.base_models import BaseModel

    
    class Review(BaseModel):
     """Represent a Review or commet inherits from BaseModel"""
       
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
