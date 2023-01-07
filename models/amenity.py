#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if (storage_type == "db"):
        name = Column(String(128), nullable=False)

    else:
        name = ""
