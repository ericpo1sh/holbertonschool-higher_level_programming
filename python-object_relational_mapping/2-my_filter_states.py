#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    search = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    database_cursor = db.cursor()
    database_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY ASC"
        .format(search)
    )
    states = database_cursor.fetchall()
    for state in states:
        print(state)
    database_cursor.close()
    db.close()
