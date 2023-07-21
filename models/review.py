#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, Integer, ForeignKey
from models.user import User


store = environ.get("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """ Review classto store review information """
    if store == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
