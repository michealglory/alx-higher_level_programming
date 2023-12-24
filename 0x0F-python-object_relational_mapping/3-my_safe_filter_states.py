#!/usr/bin/python3
"""
This script securely accepts an argument and displays all values
in the states from the hbtn_0e_0_usa database where the name matches
the provided argument. It has been designed to prevent MySQL injections.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access the database to retrieve the states.
    """
    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_position = db_connection.cursor()
    db_position.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    selected_rows = db_position.fetchall()

    for row in selected_rows:
        print(row)
