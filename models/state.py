#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="states", cascade="all, delete")

    @property
    def cities(self):
        """returns the list of City instances """

        return self.cities
