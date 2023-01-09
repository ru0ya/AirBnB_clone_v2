#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship



class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if (storage_type == "db"):
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
        user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    else:
        place_id = ""
        user_id = ""
        text = ""
