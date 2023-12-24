#!/usr/bin/python3
"""
This script establishes a State class and a Base class designed for
integration with the MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Attributes:
    __tablename__ (str): The class's table name
    id (int): The class's State ID
    name (str): The class's State name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
