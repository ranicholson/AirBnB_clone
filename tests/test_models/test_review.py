#!/usr/bin/python3
""" module containts unittests for class Review """


import unittest
import json
from models.base_model import BaseModel
from models.review import Review


class testReview(unittest.TestCase):
    """ unittests for Review """

    def setUp(self):
        """ Sets up the class """
        self.review = Review()

    def tearDown(self):
        """ Test for tear down """
        del self.review

    def test_attribute(self):
        """ Test if attributes are being saved """
        r1 = Review()
        self.assertEqual(r1.place_id, "")


if __name__ == "__main__":
    testReview()
