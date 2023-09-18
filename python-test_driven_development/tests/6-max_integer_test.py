#!/usr/bin/python3
""" Unittest for max_integer([]) """

import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    """ Test for “max at the end” exists """
    def test_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    """ Test for “max at the beginning” exists """
    def text_start(self)
        self.assertEqual(max_integer([3, 2, 1]), 3)
    """ Test for “max in the middle” exists """
    def test_middle(self)
        self.assertEqual(max_integer([2, 3, 1]), 3)
    """ test for “one negative number in the list” exists """
    def test_one_negative(self)
        self.assertEqual(max_integer([-1, 2, 3, 5]), 5)
    """ Test for “only negative numbers in the list” exists """
    def test_all_negative(self)
        self.assertEqual(max_integer([-1, -2 , -3, -4]), -1)
    """ Test for “list of one element” exists """
    def test_one_int(self)
        self.assertEqual(max_integer([80]), 80)
    """ Test for “list is empty” exists """
    def test_empty_list(self)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
