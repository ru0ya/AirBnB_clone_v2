#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    if(storage_type == "db"):
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
        reviews = relationship("Review", back_populates="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                        back_populates="place_amenities",
                                        viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = ""
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
