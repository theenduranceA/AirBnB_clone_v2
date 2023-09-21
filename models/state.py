#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """getter attribute cities that returns the list of City"""
        from models import storage
        my_list = []
        extracted_cities = storage.all(City)
        for city in extracted_cities.value():
            if city.state_id == self.id:
                my_list.append(city)
        return my_list
