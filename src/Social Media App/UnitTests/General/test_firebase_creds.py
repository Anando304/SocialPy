# imports for testing
from unittest import TestCase
import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

class TestFirebaseCreds(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_get_db(self):
        self.assertEqual(self.firebase.get_db(), self.db)

    def test_sign_in(self):
        self.assertEqual(self.firebase.get_UID(), "fwmMRSawtmYFDYm9uepJqEIjtef1")

    def test_get_user_instance(self):
        self.assertEqual(type(self.firebase.get_user_instance()), dict)

    def test_get_username(self):
        self.assertEqual(self.firebase.get_username(), "dummy")

    def test_set_username(self):
        self.firebase.set_username("dummy_new")
        self.assertEqual(self.firebase.get_username(), "dummy_new")

    def test_get_UID(self):
        # if user is logged in
        self.assertEqual(self.firebase.get_UID(), "fwmMRSawtmYFDYm9uepJqEIjtef1")

        # if user is not logged in
        firebase2 = firebase_class()
        self.assertEqual(firebase2.get_UID(), None)