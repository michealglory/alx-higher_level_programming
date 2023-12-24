#!/usr/bin/python3
"""
The script inserts the State object 'Louisiana' into the
'hbtn_0e_6_usa' database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Retrieve a state from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(db_url)
    db_session = sessionmaker(bind=db_engine)

    session = db_session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()
