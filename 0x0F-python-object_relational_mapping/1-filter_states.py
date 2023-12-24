#!/usr/bin/python3
"""
Lists all states with a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

"""
Access the database to retrieve the states.
"""

if __name__ == '__main__':
    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_position = db_connection.cursor()

    db_position.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    selected_rows = db_position.fetchall()

    for row in selected_rows:
        print(row)
