# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Firebase.Authentication import Authentication

from CommandParser.CommandParser import *

class FR_ST_2(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        # Get database instance
        self.db = self.firebase.get_db()
        self.authentication = Authentication(self.firebase,self.db)

    def test_Authentication(self):
        # Test 1: Login with valid credentials
        with mock.patch('builtins.input', return_value="dummy@gmail.com 123456789"), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.authentication.login()
            self.assertTrue("Login Successful!" in fake_out.getvalue().strip())

        # Test 2: Exit command
        with mock.patch('builtins.input', return_value="exit"), mock.patch('sys.stdout', new=StringIO()) as fake_out, self.assertRaises(SystemExit):
            self.authentication.login()
            self.assertTrue("Thanks for using SocialPy!" in fake_out.getvalue().strip())