# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.EditLocation import EditLocation

class TestEditLocation(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_EditLocation(self):
        #test to edit a location
        EditLocation(self.db, "dummy", self.user_token, "Australia")
        UpdatedLocation = self.db.child('profile').child('username').child("dummy").child("location").get(self.user_token).val()
        self.assertEqual(UpdatedLocation,"Australia")

        #test to edit location without inputting a new location
        LocationBefore = self.db.child('profile').child('username').child("dummy").child("location").get(self.user_token).val()
        EditLocation(self.db, "dummy", self.user_token, " ")
        UpdatedLocation = self.db.child('profile').child('username').child("dummy").child("location").get(self.user_token).val()
        self.assertEqual(UpdatedLocation, LocationBefore)
        

