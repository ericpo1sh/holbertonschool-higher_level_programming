#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N """
import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    database_cursor = db.cursor()
    database_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    states = database_cursor.fetchall()
    for state in states:
        print(state)
    database_cursor.close()
    db.close()
