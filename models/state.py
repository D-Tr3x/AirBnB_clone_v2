#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute returning the list of City instances"""
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
