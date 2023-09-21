#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base"""
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                'Place', secondary='place_amenity', back_populates="amenities")
    else:
        name = ""
