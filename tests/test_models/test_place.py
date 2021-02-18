#!/usr/bin/python3
""" module containts unittests for class BaseModel """


import unittest
import json
from models.base_model import BaseModel
from models.place import Place


class testPlace(unittest.TestCase):
    """ unittests for Place """

    def setUp(self):
        """ Sets up the class """
        self.place = Place()

    def tearDown(self):
        """ Test for tear down """
        del self.place

    def test_attributes(self):
        """ Test for saved attributes """
        p1 = Place()
        self.assertEqual(p1.city_id, "")



if __name__ == "__main__":
    testPlace()
