# imports for testing
import unittest
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class FR_ST_13(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def testCommandParser(self):
        running = [True]
        command_parser = CommandParser(running, self.firebase, self.db)
        command_parser.parseCommand("profile edit_name NotDummy")
        name = self.db.child('profile').child('username').child('dummy').child('name').get(self.user_token).val()
        self.assertEqual(name,"notdummy")
        command_parser.parseCommand("profile edit_name dummy")
