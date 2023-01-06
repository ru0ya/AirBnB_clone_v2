#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column("user_id", String(60), nullable=False, ForeignKey('users.id'))
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=0.0)
    longitude = Column(Float, nullable=True, default=0.0)
    amenity_ids = []
