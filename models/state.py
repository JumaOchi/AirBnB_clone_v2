#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

    def cities(self):
        """Returns list of cities"""
        the_cities = []
        for c in models.storage.all(City).values():
            if c.state_id == self.id:
                the_cities.append(c)
        return the_cities
