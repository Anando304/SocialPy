# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.EditName import EditName

class TestEditName(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_EditName(self):
        #test to edit a name
        EditName(self.db, "dummy", self.user_token, "dummy1")
        UpdatedName = self.db.child('profile').child('username').child("dummy").child("name").get(self.user_token).val()
        self.assertEqual(UpdatedName,"dummy1")

        #test to edit name without inputting a new name
        NameBefore = self.db.child('profile').child('username').child("dummy").child("name").get(self.user_token).val()
        EditName(self.db, "dummy", self.user_token, " ")
        UpdatedName = self.db.child('profile').child('username').child("dummy").child("name").get(self.user_token).val()
        self.assertEqual(UpdatedName, NameBefore)
        