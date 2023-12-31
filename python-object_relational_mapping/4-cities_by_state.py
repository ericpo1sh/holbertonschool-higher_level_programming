#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """


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
    database_cursor.execute(
        "\
        SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id ASC\
        "
    )
    output = database_cursor.fetchall()
    for object in output:
        print(object)
    database_cursor.close()
    db.close()
