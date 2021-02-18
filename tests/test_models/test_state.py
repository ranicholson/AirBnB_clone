#!/usr/bin/python3
""" module containts unittests for class State """


import unittest
import json
from models.base_model import BaseModel
from models.state import State


class testState(unittest.TestCase):
    """ unittests for State """

    def setUp(self):
        """ Sets up the class """
        self.state = State()

    def tearDown(self):
        """ Test for tear down """
        del self.state

    def test_attribute(self):
        """ Test for saved attributes """
        s1 = State()
        self.assertEqual(s1.name, "")

if __name__ == "__main__":
    testState()
