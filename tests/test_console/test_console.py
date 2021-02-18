#!/usr/bin/python3
""" module containts unittests for our console """


import unittest
import json
from .models.base_model import BaseModel
from .models.engine.file_storage import FileStorage


class testconsole(unittest.TestCase):

    """ unittests for console """

    def test_created_console(self):
        """ Datetime at creation of an object from console """

    def test_updated_console(self):
        """ Datetime at update of an object from console """

    def test_create(self):
        """ Test creation of new instances in the console """

    def test_show(self):
        """ Test retrieval of data from show command """

    def test_destroy(self):
        """ Test to destroy instance from file storage """

    def test_all(self):
        """ Tests printing of all instances in storage with attributes """

    def test_update(self):
        """ Test update of instances from the console """

    def test_EOF(self):
        """ EOF to quit console """

    def test_help(self):
        """ Test help commnand to display details of commands in console """

    def test_quit(self):
        """ Test that quit exits console """


if __name__ == "__main__":
    testConsole()
