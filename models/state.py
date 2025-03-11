#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import Base
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    class State(BaseModel, Base):
        """ State class for DB storage """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
else:
    class State(BaseModel):
        """ State class for file storage """
        name = ""

        @property
        def cities(self):
            """Getter attribute returning the list of City instances"""
            from models.city import City
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
