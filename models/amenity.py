#!/usr/bin/python3
""" Amenity Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base"""
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
