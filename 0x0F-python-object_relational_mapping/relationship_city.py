#!/usr/bin/python3
"""
This script establishes a City class designed for integration
with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """tablename (str): The table name associated with the class
    id (int): The identifier of the class
    name (str): The name associated with the class
    state_id (int): The identifier of the state to which the city belongs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
