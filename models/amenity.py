#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    class Amenity(BaseModel, Base):
        """ Represents an Amenity for MySQL database """
        __tablename__ = "amenities"
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1',
            'mysql_collate': 'latin1_swedish_ci'
        }

        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            viewonly=False,
            back_populates="amenities",
            overlaps="amenities"
        )
else:
    class Amenity(BaseModel):
        """ Represents an Amenity for FileStorage """
        name = ""
