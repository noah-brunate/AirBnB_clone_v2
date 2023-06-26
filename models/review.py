#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from os import environ
from sqlalchemy import Column, String, Integer, ForiegnKey


store = environ.get("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """ Review classto store review information """
    if store == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey(Place.id))
        user_id = Column(String(60), nullable=False, ForeignKey(User.id))
    else:
        place_id = ""
        user_id = ""
        text = ""
