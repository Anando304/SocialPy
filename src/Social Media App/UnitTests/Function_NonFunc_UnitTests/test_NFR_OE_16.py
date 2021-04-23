# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class NFR_OE_16(TestCase):

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

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            try:
                command_parser.parseCommand("post view dummy")
                # if there was no error, command connected to the database properly so assert True
                self.assertTrue(True)
            except:
                self.assertTrue(False)
