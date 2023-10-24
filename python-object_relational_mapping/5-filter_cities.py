#!/usr/bin/python3
""" Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database """


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
        "\
        SELECT cities.name, states.name \
        FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id ASC\
        "
    )
    output = database_cursor.fetchall()
    print_all = [object[0] for object in output if object[1] == search]
    print(", ".join(print_all))

    database_cursor.close()
    db.close()
