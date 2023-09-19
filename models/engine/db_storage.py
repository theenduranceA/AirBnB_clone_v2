#!/usr/bin/python3
"""This module defines the engine for the MySQL database"""
from models.base_model import BaseModel, Base
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """defining the class DBStorage"""

    __clases = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
    if env == "test":
        Base.Metadata.drop_all()

    def all(self, cls=None):
        """Method to return a dictionary of object"""
        my_dict = {}
        if cls in self.__clases:
            result = DBStorage.__session.query(cls)
            for row in result:
                key = "{}.{}".format(row.__class__.name__, row.id)
                my_dict[key] = row
        elif cls is None:
            for cl in self.__clases:
                result = DBStorage.__session.query(cl)
                for row in result:
                    key = "{}.{}".format(row.__class__.name__, row.id)
                    my_dict[key] = row
        return my_dict

    def new(self, obj):
        """Method to add new object to the cuurrent database"""
        DBStorage.__session.add(obj)

    def save(self):
        """methid to commit all changes to the current database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Method to delete an object in the current database"""
        DBStorage.__session.delete(obj)

    def reload(self):
        """method to create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def close(self):
        """Public Method to call remove method"""
        DBStorage.__session.close()
