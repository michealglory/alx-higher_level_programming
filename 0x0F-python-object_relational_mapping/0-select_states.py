#!/usr/bin/python3
"""
Lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Retrieve states from the database.
    """
    db_connection = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_position = db_connection.cursor()

    db_position.execute("SELECT * FROM states")

    selected_rows = db_position.fetchall()

    for row in selected_rows:
        print(row)
