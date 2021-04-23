# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class NFR_PR_10(TestCase):

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

        # check if post added succussfully
        # store the printed console items in the fake_out variable for assertions later
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            command_parser.parseCommand("post add Hello there! My name is Dummy and this is a test post!!")

            # delete the post that was just added
            posts = QueryPostsByUser(self.db, "dummy", self.user_token)
            for post in posts:
                if post["content"] == "Hello there! My name is Dummy and this is a test post!!":
                    DeletePost(self.db, self.firebase.get_username(), self.user_token, post["post_id"])

            # check if post succuss message was printed to console
            self.assertTrue('Post "Hello there! My name is Dummy and this is a test post!!" added' in fake_out.getvalue().strip())