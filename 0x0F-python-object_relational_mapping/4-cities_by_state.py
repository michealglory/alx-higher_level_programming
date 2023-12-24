#!/usr/bin/python3
"""
This script enumerates all cities from the hbtn_0e_4_usa database.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database to retrieve the cities.
    """

    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connection.cursor() as db_position:
        db_position.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        selected_rows = db_position.fetchall()

    if selected_rows is not None:
        for row in selected_rows:
            print(row)
