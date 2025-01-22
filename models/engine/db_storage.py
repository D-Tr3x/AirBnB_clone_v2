#!/usr/bin/python3
"""This module implements a new engine: DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class representing a new engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links it to MySQL database"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session

        If cls is None, query all types of objects

        Return:
            dictionary of objects in format <class-name>.<object-id> = obj
        """
        my_dict = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    my_dict[key] = obj.to_dict()
        else:
            if cls in classes:
                query = self.__session.query(cls)
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    my_dict[key] = obj.to_dict()

        return my_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session `obj` if not `None`"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
