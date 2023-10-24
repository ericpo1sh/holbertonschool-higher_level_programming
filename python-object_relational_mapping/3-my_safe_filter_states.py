#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections"""
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
    database_cursor.execute("SELECT * FROM states ORDER BY ASC")
    states = database_cursor.fetchall()
    for state in states:
        if state[1] == search:
            print(state)
    database_cursor.close()
    db.close()
