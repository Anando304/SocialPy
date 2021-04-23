# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.QueryPosts import *

class TestQueryPosts(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_QueryPosts(self):
        # Test 1: Attempting to Query Profile of blank account
        query1 = QueryPostsByUser(self.db, "", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: Attempting to Query Posts of invalid username
        query2 = QueryPostsByUser(self.db, "justin trudeau", self.user_token)
        self.assertEqual(query2, None)

        # Test 3: Attempting to Query posts validly
        validQuery1 = QueryPostsFollowers(self.db, self.firebase, self.user_token)
        validQuery2 = QueryPostsFollowing(self.db, self.firebase, self.user_token)
        validQuery3 = QueryPostsAll(self.db, self.user_token)
        self.assertEqual(type(validQuery1), dict)
        self.assertEqual(type(validQuery2), dict)
        self.assertEqual(type(validQuery3), list)