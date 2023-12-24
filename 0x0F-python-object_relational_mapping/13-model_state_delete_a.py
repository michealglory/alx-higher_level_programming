#!/usr/bin/python3
"""
The script removes all State objects with a name containing the letter
'a' from the 'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    This script deletes State objects from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(db_url)
    db_session = sessionmaker(bind=db_engine)

    session = db_session()

    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            session.delete(state)

    session.commit()

    session.close()
