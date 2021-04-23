# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.ViewProfile import ViewProfile

class TestViewProfile(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_ViewProfile(self):
        # Test 1: Attempting to view Profile of blank account
        query1 = ViewProfile(self.db, " ", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: Attempting to view Profile of invalid username
        query2 = ViewProfile(self.db, "justin trudeau", self.user_token)
        self.assertEqual(query2, None)

        # Test 3: Attempting to view a valid profile
        try:
            ViewProfile(self.db, "dummy", self.user_token)
            # if there was no error, profile was printed properly so assert True
            self.assertTrue(True)
        except:
            self.assertTrue(False)