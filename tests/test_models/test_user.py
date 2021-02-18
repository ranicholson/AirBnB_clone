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
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")

    def test_id(self):
        """ tests id is there """
        a1 = User()
        self.assertIsNotNone(a1.id)

    def test_storage(self):
        """ Test for storage of user data """
        pass

if __name__ == "__main__":
    testUser()
