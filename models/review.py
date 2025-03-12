#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.base_model import BaseModel, Base
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    class Review(BaseModel, Base):
        """ Represents the review for the HBNB """
        __tablename__ = "reviews"
        __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'latin1',
            'mysql_collate': 'latin1_swedish_ci'
        }

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
else:
    class Review(BaseModel):
        """ Represents a Review for file storage """
        text = ""
        place_id = ""
        user_id = ""
