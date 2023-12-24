#!/usr/bin/python3
"""
This script accepts the name of a state as an argument and lists
all cities of that state using the 'hbtn_0e_4_usa' database.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Retrieve city information from the database.
    """

    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connection.cursor() as db_position:
        db_position.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        selected_rows = db_position.fetchall()

    if selected_rows is not None:
        print(", ".join([row[1] for row in selected_rows]))
