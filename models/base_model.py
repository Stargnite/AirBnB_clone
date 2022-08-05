#!/usr/bin/python3 
"""Difine the BaseModel"""
import models
from uuid import uuid4
from datetime import datetime

   class BaseModel:
     """ BaseModel of the Airbnb clone Project."""
     
    def __int__(self, *args, *kwargs):
      """BaseModel Construction"""
      
      if len(kwargs) == 0:
         self.id = str(uuid4())
         self.create_at = datetime.now()
         self.update_at = self.create_at
         models.storage.new(self)
         model.storage(save)
      else: 
        format = "%Y-%m-%dt-%H:%M:%S.%f"
        kwargs["create_at"] = datetime.strptime(kwargs["creat_at"], format)
        kwargs["update_at"] = datetime.strptime(kwargs["update_at"], format)
        for key, val in kwargs.item()
            if "__class__" not in key:
              setattr(self, key, val)
              
      def __str__(self):
        """
           print the isinstance
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
        def self(save):
          """
              update the public instance attrivutes
         """
         self.update_at = datetime.now()
         models.storage.save()
         
        def to_dict(self):
          """
             Returne a Dictinary containing values/ all keys of __dict__ instance
          """
        
        new_dict = dict(self.__dict__)
        new_dict = ["create_at"] = self.create_at.isoformat(sep='T')
        new_dict = ["update_ta"] = self.update_at.isoformat(sep='T')
        new_dict = ["__class__"] = self.class.__name__
        return new_dict
