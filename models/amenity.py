#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
<<<<<<< HEAD
from sqlalchemy import ForeignKey
=======
>>>>>>> 0778974c353f927319c26f2301f32a2a98ee57c8
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if (storage_type == "db"):
        name = Column(String(128), nullable=False)


    else:
        name = ""

class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table amenities.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

