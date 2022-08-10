import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))
    email = Column(String(250), unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    hair_color = Column(String(100))
    mass = Column(String(250))
    gender = Column(String(250))
    vehicle_id = Column(Integer,ForeignKey('vehicles.id'))

class Planets(Base):
    __tablename__ = 'characters'


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')