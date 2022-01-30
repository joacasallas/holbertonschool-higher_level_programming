#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_function(self):
        list1 = [1, 2, 3, 4]
        list2 = [4, 2, 3, 4]
        list3 = [1, 4, 3]
        list4 = [1, -3, 4]

        for i in range(len(list4)):
            if list4[i] < 0:
                list4[i] *= -1
        self.assertEqual(max_integer(list1), 4)
        self.assertEqual(max_integer(list2), 4)
        self.assertEqual(max_integer(list3), 4)
        self.assertEqual(max_integer(list4), 4)
