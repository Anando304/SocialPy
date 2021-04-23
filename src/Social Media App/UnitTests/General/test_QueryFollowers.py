# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.QueryFollowers import QueryFollowers, QueryFollowing

class TestQueryFollowers(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_QueryFollowers(self):
        # Test 1: Attempting to Query followerslist of blank user
        query1 = QueryFollowers(self.db, "", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: Attempting to Query followerslist of invalid user
        query2 = QueryFollowers(self.db, "jeff bezos", self.user_token)
        self.assertEqual(query2, None)

        # Test 3: Attempting to Query followerslist of valid user with no followings
        # reset list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"followers_list": ""},self.user_token)
        query3 = QueryFollowers(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query3, "")

        # Test 4: Attempting to Query followerslist of valid user with atleast one following
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"followers_list": "graeme"},self.user_token)
        query4 = QueryFollowers(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query4, ["graeme"])
        # reset the following list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"followers_list": ""},self.user_token)

        # Test 5: Attempting to Query followerslist of valid user with multiple users
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"followers_list": "graeme, yuvi"},self.user_token)
        query4 = QueryFollowers(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query4, ['graeme', ' yuvi'])
        # reset list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"followers_list": ""},self.user_token)



    def test_QueryFollowing(self):
        # Test 1: Attempting to Query following List of blank user
        query1 = QueryFollowing(self.db, "", self.user_token)
        self.assertEqual(query1, None)

        # Test 2: Attempting to Query following List of invalid user
        query2 = QueryFollowing(self.db, "jeff bezos", self.user_token)
        self.assertEqual(query2, None)

        # Test 3: Attempting to Query following list of valid user with no followings
        # reset list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"following_list": ""},self.user_token)
        query3 = QueryFollowing(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query3, "")

        # Test 4: Attempting to Query following list of valid user with atleast one following
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"following_list": "graeme"},self.user_token)
        query4 = QueryFollowing(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query4, ["graeme"])
        # reset the following list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"following_list": ""},self.user_token)

        # Test 5: Attempting to Query following list of valid user with multiple users
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"following_list": "graeme, yuvi"},self.user_token)
        query4 = QueryFollowing(self.db, self.firebase.get_username(), self.user_token)
        self.assertEqual(query4, ['graeme', ' yuvi'])
        # reset list
        self.db.child("profile").child("username").child(self.firebase.get_username()).child("following").update({"following_list": ""},self.user_token)