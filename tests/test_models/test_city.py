#!/usr/bin/python3
""" module containts unittests for class City """


import unittest
import json
from models.base_model import BaseModel
from models.city import City


class testCity(unittest.TestCase):
    """ unittests for City """

    def setUp(self):
        """ Sets up the class """
        self.city = City()

    def tearDown(self):
        """ Test for tear down """
        del self.city

    def test_attributes(self):
        """ test for saved attributes """
        c1 = City()
        self.assertEqual(c1.state_id, "")


if __name__ == "__main__":
    testCity()
