#!/usr/bin/python3
""" module containts unittests for class BaseModel """


import unittest
import json
from models.base_model import BaseModel
from models.user import User


class testUser(unittest.TestCase):
    """ unittests for class User """

    def setUp(self):
        """ Sets up the object in class user """
        self.user = User()

    def tearDown(self):
        """ Test for user tear down """
        del self.user

    def test_attribute(self):
        """ Test for saved attributes """
        u1 = User()
        self.assertEqual(u1.email, "")


if __name__ == "__main__":
    testUser()
