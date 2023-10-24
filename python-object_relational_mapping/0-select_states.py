#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa: """
import MySQLdb
from sys import argv


def list_states():
    """ Selects each state from database """

    username = argv[1]
    passwd = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=passwd,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT states.name FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()
    for statename in states:
        print(statename)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
