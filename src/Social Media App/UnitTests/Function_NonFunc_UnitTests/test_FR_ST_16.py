# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class FR_ST_16(TestCase):

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
        command_parser.parseCommand("profile followers_view anando")
        followersList = self.db.child('profile').child('username').child('anando').child('following').child("followers_list").get(self.user_token).val()
        self.assertEqual(followersList,'graeme')