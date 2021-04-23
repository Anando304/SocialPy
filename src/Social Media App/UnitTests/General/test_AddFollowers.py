# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.AddFollowers import AddFollowers
from Profile.QueryFollowers import QueryFollowing

class TestAddFollowers(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_AddFollowers(self):
        # Test 1: Attempting to add username as empty
        with mock.patch('Profile.AddFollowers.QueryFollowing', return_value={"graeme"}), mock.patch('Profile.AddFollowers.QueryFollowers', return_value={self.firebase.get_username()}), mock.patch('sys.stdout', new = StringIO()) as fake_out:
            AddFollowers(self.db, self.firebase.get_username(), "", self.user_token)
            self.assertEqual(fake_out.getvalue().strip(), "User to follow cannot be blank. You must enter a valid username to follow")

        # Test 2: Attempting to add a valid user to following list
        with mock.patch('Profile.AddFollowers.QueryFollowing', return_value={""}), mock.patch('Profile.AddFollowers.QueryFollowers', return_value={""}), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            # add a user to follow to the dummy account
            AddFollowers(self.db, self.firebase.get_username(), "graeme", self.user_token)
            # Query the data
            query_updated_data = QueryFollowing(self.db, self.firebase.get_username(), self.user_token)
            # Now check if right output is in DB
            self.assertEqual(query_updated_data, ['graeme'])

        # Test 3: Attempt to add yourself to following list
        with mock.patch('Profile.AddFollowers.QueryFollowing', return_value={""}), mock.patch('Profile.AddFollowers.QueryFollowers', return_value={""}), mock.patch('sys.stdout',new=StringIO()) as fake_out:
            AddFollowers(self.db, self.firebase.get_username(), self.firebase.get_username(), self.user_token)
            self.assertEqual(fake_out.getvalue().strip(),"You cannot follow yourself. Please try following a valid user other than yourself.")

        # Test 4: Attempt to add someone who does not exist in the system
        with mock.patch('Profile.AddFollowers.QueryFollowing', return_value={""}), mock.patch('Profile.AddFollowers.QueryFollowers', return_value={}), mock.patch('sys.stdout',new=StringIO()) as fake_out:
            AddFollowers(self.db, self.firebase.get_username(), "mark zuckerberg", self.user_token)
            self.assertEqual(fake_out.getvalue().strip(),"There is no user with the username mark zuckerberg")