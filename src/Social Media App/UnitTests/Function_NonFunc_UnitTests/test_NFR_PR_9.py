# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.QueryPosts import QueryPostsByUser

class NFR_PR_9(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_NFR_PR_9(self):
        query = QueryPostsByUser(self.db, "dummy", self.user_token)
        time = query[0].get("time")
        self.assertEqual(time,"03/31/2021")
