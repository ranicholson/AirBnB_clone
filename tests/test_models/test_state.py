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

    def testId(self):
        """ Tests id """

    def test_created_at(self):
        """ Datetime at creation of an object """

    def test_updated_at(self):
        """ Datetime at update of an object """

    def test_str(self):
        """ Test that str prints details correctly """

    def test_to_dict(self):
        """ Test that keys/values are saving correctly """

    def test_save(self):
        """ Tests that instance attributes are saved and updated
        correctly with the proper updated datetime """


if __name__ == "__main__":
    testState()