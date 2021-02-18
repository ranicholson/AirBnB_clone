#!/usr/bin/python3
""" module containts unittests for class BaseModel """


import unittest
import json
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """ unittests for BaseModel """

    def setUp(self):
        """ Sets up the class """
        self.velour = BaseModel()
        self.velour1 = BaseModel(name="Sasha")
        self.velour2 = BaseModel(name="Sasha", id="None")
        self.velour3 = BaseModel(name="Sasha", number="2020")
        self.velour4 = BaseModel(name="", number="None", id="None")
        self.velour5 = BaseModel()

    def tearDown(self):
        """ Tears down """
        del self.velour

    def testId(self):
        """ Tests id for uniqueness """
        self.assertNotEqual(self.velour.id, self.velour1.id)
        self.assertNotEqual(self.velour.id, self.velour2.id)
        self.assertNotEqual(self.velour2.id, self.velour3.id)
        self.assertNotEqual(self.velour3.id, self.velour4.id)
        self.assertNotEqual(self.velour4.id, self.velour5.id)
        self.assertNotEqual(self.velour1.id, self.velour2.id)

    def test_custom(self):
        """ test for custom attributes """
        self.velour.hello = "world"
        self.assertEqual(self.velour.hello, "world")

    def test_noupdateId(self):
        """ test """
        self.velour = BaseModel(2020)
        self.assertNotEqual(self.velour.id, 2020)
        self.velour = BaseModel(123)
        self.assertNotEqual(self.velour.id, 123)
        self.velour = BaseModel(1)
        self.assertNotEqual(self.velour.id, 1)

    def testId_match(self):
        self.velour.name = "Sasha"
        self.velour.champion = 2017

        self.assertIsNotNone(self.velour.id)
        self.assertEqual(self.velour.name, "Sasha")
        self.assertEqual(self.velour.champion, 2017)

    def test_str(self):
        """ Test that str prints details correctly """
        pass

    def test_to_dict(self):
        """ Test that keys/values are saving correctly """
        pass

    def test_save(self):
        """ Tests that instance attributes are saved and updated
        correctly with the proper updated datetime """
        pass


if __name__ == "__main__":
    testBaseModel()
