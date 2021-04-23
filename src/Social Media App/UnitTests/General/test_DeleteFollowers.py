# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.DeleteFollowers import DeleteFollowers

class TestDeleteFollowers(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_DeleteFollowers(self):
        # Test 1: Attempting to Delete user that is blank
        with mock.patch('Profile.DeleteFollowers.QueryFollowing', return_value={"graeme"}), mock.patch('Profile.DeleteFollowers.QueryFollowers', return_value={self.firebase.get_username()}), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            DeleteFollowers(self.db, self.firebase.get_username(), "", self.user_token)
            self.assertEqual(fake_out.getvalue().strip(), "User to follow cannot be blank. You must enter a valid username to remove")

        # Test 2: Attempting to delete a user that does not exist in the system
        with mock.patch('Profile.DeleteFollowers.QueryFollowing', return_value={"graeme"}), mock.patch('Profile.DeleteFollowers.QueryFollowers', return_value={self.firebase.get_username()}), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            DeleteFollowers(self.db, self.firebase.get_username(), "mark zuckerberg", self.user_token)
            self.assertEqual(fake_out.getvalue().strip(),"There is no user with the username mark zuckerberg")

        # Test 3: Attempting to delete a user that exists but that is not in your followinglist!
        with mock.patch('Profile.DeleteFollowers.QueryFollowing', return_value={"graeme"}), mock.patch('Profile.DeleteFollowers.QueryFollowers', return_value={self.firebase.get_username()}), mock.patch('sys.stdout', new = StringIO()) as fake_out:
            DeleteFollowers(self.db, self.firebase.get_username(), "yuvi", self.user_token)
            self.assertEqual(fake_out.getvalue().strip(),"Sorry, yuvi does not exist in your following list!")

        # Test 4: Attempting to delete a user that exists in your followinglist!
        with mock.patch('Profile.DeleteFollowers.QueryFollowing', return_value={"graeme"}), mock.patch('Profile.DeleteFollowers.QueryFollowers', return_value={self.firebase.get_username()}):
            DeleteFollowers(self.db, self.firebase.get_username(), "graeme", self.user_token)