#!/usr/bin/python3

"""
This module contains unittests for the console.py module
"""

import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestHBNBCommand_prompt(unittest.TestCase):
    """Tests the prompt of the console if it is 
    (hbnh) as wanted
    """

    def test_prompt_style(self):
        """The string used as prompt style"""
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)

    def test_emptyline(self):
        """Test what show happen when no input is given to condole"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", out.getvalue().strip())




class TestHBNBCommand_help(unittest.TestCase):
    """This set of tests checks for proper out of the documentation"""

    def test_help(self):
        """Check the cmd.Cmd parent class help feature along side 
        the console overwritten help function?method
        """
        res = ("Documented commands (type help <topic>):"
               "\n========================================"
                "\nEOF  all  all2  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(res, out.getvalue().strip())



class TestHBNBCommand_exits(unittest.TestCase):
    """This set of tests checks for proper output of the exits commands"""

    def test_quit(self):
        """Check the quit command for proper functionality
        """

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Check the EOF command for proper functionality
        """

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertTrue(HBNBCommand().onecmd("EOF"))



class TestHBNBCommand_create(unittest.TestCase):
    """This set of tests checks the create command  in HBNBCommands"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass


    def test_create_Err1(self):
        """Expected error if class name is missing
        """
        err = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(err, out.getvalue().strip())


    def test_create_Err2(self):
        """Expected error if class doesn't exist
        """
        err = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create Fake"))
            self.assertEqual(err, out.getvalue().strip())


    def test_create_Err3(self):
        """Expected error if class name is missing
        """
        err = "*** Unknown syntax: Fake.create"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("Fake.create"))
            self.assertEqual(err, out.getvalue().strip())


    def test_create_Err4(self):
        """Expected error if class name is missing
        """
        err = "*** Unknown syntax: Basemodel.create"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("Basemodel.create"))
            self.assertEqual(err, out.getvalue().strip())


    def test_create_obj(self):
        """Expected create to create objs
        """

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("User.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("Place.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("Amenity.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("State.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("City.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(out.getvalue().strip()))
            testid = ("Review.{}".format(out.getvalue().strip()))
            self.assertIn(testid, storage.all().keys())



class TestHBNBCommand_help(unittest.TestCase):
    """This set of tests checks for proper out of the documentation"""

    def test_help(self):
        """Check the cmd.Cmd parent class help feature along side 
        the console overwritten help function?method
        """
        res = ("Documented commands (type help <topic>):"
               "\n========================================"
                "\nEOF  all  all2  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(res, out.getvalue().strip())
