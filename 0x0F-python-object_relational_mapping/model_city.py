#!/usr/bin/python3
"""
The script defines a City class for interaction with the MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class with attributes:
    - __tablename__ (str): The table name of the class
    - id (int): The id of the city
    - name (str): The name of the city
    - state_id (int): The id of the state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
