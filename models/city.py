#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if (storage_type == "db"):
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
        places = relationship('Place', backref='cities',
                                cascade='all, delete, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
