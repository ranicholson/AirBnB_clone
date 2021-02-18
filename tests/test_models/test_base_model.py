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
        self.velour4 = BaseModel(name="", number="None", id="")
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

        self.assertIsInstance(self.velour.id, str)

    def test_custom(self):
        """ test for custom attributes """
        self.velour.hello = "world"
        self.assertEqual(self.velour.hello, "world")

#    def test_created_at(self):
#        """ Test that datetime updates at creation """
#        self.assertIsInstance(self.velour.created_at, datetime)
#        self.assertIsInstance(self.velour1.created_at, datetime)
#        self.assertIsInstance(self.velour2.created_at, datetime)
#        self.assertIsInstance(self.velour3.created_at, datetime)
#        self.assertIsInstance(self.velour4.created_at, datetime)
#        self.assertIsInstance(self.velour5.created_at, datetime)

    def test_noupdateId(self):
        """ test """
        self.velour = BaseModel(2020)
        self.assertNotEqual(self.velour.id, 2020)
        self.velour = BaseModel(123)
        self.assertNotEqual(self.velour.id, 123)
        self.velour = BaseModel(1)
        self.assertNotEqual(self.velour.id, 1)

    def test_Id_match(self):
        """ test for matching id """
        self.velour.name = "Sasha"
        self.velour.champion = 2017

        self.assertIsNotNone(self.velour.id)
        self.assertEqual(self.velour.name, "Sasha")
        self.assertEqual(self.velour.champion, 2017)

    def test_str(self):
        """ Test that str prints details correctly """
        pass

#    def test_to_dict(self):
#        """ Test that dict is saving all keys/values """
#        self.assertTrue('id' in dir(self.velour))
#        self.assertTrue('created_at' in dir(self.velour))
#        self.assertTrue('updated_at' in dir(self.velour))
#        self.assertTrue('to_dict' in dir(self.velour))
#        self.assertTrue('save' in dir(self.velour))

#        velour1_list = dir(self.velour1)
#        test = 'to_dict' in velour1_list
#        self.assertTrue(test)
#        test = 'created_at' in velour1_list
#        self.assertTrue(test)
#        self.assertTrue('updated_at' in dir(self.velour1))
#        self.assertTrue('id' in dir(self.velour1))
#        self.assertTrue('save' in dir(self.velour1))

    def test_dictToObject(self):
        """ Tests type from obj to dict to obj """
        self.assertIsNot(type(self.velour), dict)
        self.assertIsNot(type(self.velour1), dict)
        self.assertIsNot(type(self.velour2), dict)
        self.assertIsNot(type(self.velour3), dict)
        self.assertIsNot(type(self.velour4), dict)
        self.assertIsNot(type(self.velour5), dict)

        velour_j = self.velour.to_dict()
#        velour1_j = self.velour1.to_dict()
#        velour2_j = self.velour2.to_dict()
#        velour3_j = self.velour3.to_dict()
#        velour4_j = self.velour4.to_dict()
#        velour5_j = self.velour5.to_dict()

        self.assertIs(type(velour_j), dict)
#        self.assertIs(type(velour1_j), dict)
#        self.assertIs(type(velour2_j), dict)
#        self.assertIs(type(velour3_j), dict)
#        self.assertIs(type(velour4_j), dict)
#        self.assertIs(type(velour5_j), dict)

if __name__ == "__main__":
    testBaseModel()
