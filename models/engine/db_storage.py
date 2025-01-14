#!/usr/bin/python3
"""This module defines the engine for the MySQL database"""
from models.base_model import Base
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
my_classes = {
    'Amenity': Amenity,
    'City': City,
    'User': User,
    'Place': Place,
    "State": State,
    'Review': Review,
}


class DBStorage:
    """defining the class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to return a dictionary of object"""
        my_dict = {}
        if cls is None:
            for my_cls in my_classes.values():
                if self.__session.query(my_cls).all():
                    for item in self.__session.query(my_cls).all():
                        my_dict[item.id] = item
        else:
            for item in self.__session.query(my_classes[cls]):
                my_dict[item.id] = item
        return (my_dict)

    def new(self, obj):
        """Method to add new object to the cuurrent database"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """methid to commit all changes to the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete an object in the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """method to create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Calls close"""
        self.__session.close()
