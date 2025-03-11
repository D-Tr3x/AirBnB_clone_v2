#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import Base, BaseModel
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):
        """ The city class for DB storage, contains state ID and name """
        __tablename__ = 'cities'

        id = Column(String(60), primary_key=True, nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
else:
    class City(BaseModel):
        """ The city class for FileStorage """
        state_id = ""
        name = ""
        place = []
