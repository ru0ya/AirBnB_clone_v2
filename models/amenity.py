#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from models import storage_type


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table amenities.
    Attributes:
    __tablename__ (str): The name of the MySQL table to store Amenities.
    name (sqlalchemy String): The amenity name.
    place_amenities (sqlalchemy relationship): Place-Amenity relationship.
      """

    __tablename__ = "amenities"
    if (storage_type == "db"):
        name = Column(String(128), nullable=False)

    else:
        name = ""
