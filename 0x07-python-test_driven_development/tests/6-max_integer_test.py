#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_function(self):
        self.assertTrue([1, 4, 5], 5)
        self.assertTrue([5, 4, 1], 5)
        self.assertTrue([4, 5, 1], 5)
