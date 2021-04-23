# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.QueryProfile import QueryProfile

class TestQueryProfile(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_QueryProfile(self):
        # Test 1: Attempting to Query Profile of blank account
        query1 = QueryProfile(self.db, " ", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: Attempting to Query Profile of invalid username
        query2 = QueryProfile(self.db, "justin trudeau", self.user_token)
        self.assertEqual(query2, None)

        # Test 3: Attempting to Query a valid profile
        query3 = QueryProfile(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(type(query3), dict)