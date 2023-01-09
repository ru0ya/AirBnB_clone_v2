#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models import storage_type
from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

if storage_type == "db":
    place_amenity = Table("place_amenity", Base.metadata,
            Column("place_id", String(60), ForeignKey("places.id"),
                primary_key=True, nullable=False),
            Column("amenity_id", String(60), ForeignKey("amenities.id"), 
                primary_key=True, nullable=False))


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

        @property
        def reviews(self):
            """returns list of review instances with place_id
            equals to current Place.id
            FileStorage relationship between Place and Review
            """
            from models import storage
            all_revs = storage.all(Review)
            cl = []
            for rev in all_revs.values():
                if rev.place_id == self.id:
                    cl.append(rev)
            return cl

        @property
        def amenities(self):
            """returns list of Amenity instances based
            on attribute amenity_ids that contain all
            Amenity.id linked to it"""
            from models import storage
            all_amen = storage.all(Amenity)
            cl = []
            for amen in all_amen.values():
                if amen.id in self.amenity_ids:
                    cl.append(amen)
            return cl

        @amenities.setter
        def amenities(self, obj):
            """method that adds an Amenity.id to the
            attribute amenity_ids accepting only Amenity 
            objects"""
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
