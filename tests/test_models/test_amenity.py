#!/usr/bin/python3
""" module containts unittests for class Amenity """


import unittest
import json
from models.base_model import BaseModel
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """ unittests for BaseModel """

    def setUp(self):
        """ Sets up the class """
        self.amenity = Amenity()

    def tearDown(self):
        """ Test for tear down """
        del self.amenity

    def test_assignment(self):
        """ assign a value to the class attributes """
        a1 = Amenity()
        self.assertEqual(a1.name, "")


if __name__ == "__main__":
    testAmenity()
