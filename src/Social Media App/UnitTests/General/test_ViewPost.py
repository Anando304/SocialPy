# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.ViewPost import *


class TestViewPost(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_ViewPost(self):
        # Test 1: View posts from null user
        query1 = ViewPostsByUser(self.db, "", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: View posts from a real user
        try:
            ViewPostsByUser(self.db, "dummy", self.user_token)
            # if there was no error, posts were printed properly so assert True
            self.assertTrue(True)
        except:
            self.assertTrue(False)

        # Test 3: ViewPostsFollowing
        try:
            ViewPostsFollowing(self.db, self.firebase, self.user_token)
            # if there was no error, posts were printed properly so assert True
            self.assertTrue(True)
        except:
            self.assertTrue(False)

        # Test 4: ViewPostsAll
        try:
            ViewPostsAll(self.db, self.user_token)
            # if there was no error, posts were printed properly so assert True
            self.assertTrue(True)
        except:
            self.assertTrue(False)



