#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ initializing MyList Class """
    def print_sorted(self):
        """ print_sorted function created """
        print(sorted(self))
