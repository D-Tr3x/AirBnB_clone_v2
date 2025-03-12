#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import Base, BaseModel
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    class User(BaseModel, Base):
        """Represents a user for HBNB in MySQL database"""
        __tablename__ = "users"
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1',
            'mysql_collate': 'latin1_swedish_ci'
        }


        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
else:
    class User(BaseModel):
        """Represents a user for FileStorage"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        places = []
        reviews = []
