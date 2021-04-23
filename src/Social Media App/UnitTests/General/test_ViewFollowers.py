# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Profile.ViewFollowers import ViewFollowers
from Profile.ViewFollowers import ViewFollowing

class TestViewFollowers(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_ViewFollowing(self):
        #test to see following
        # store the printed console items in the fake_out variable for assertions later
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowing(self.db, "graeme", self.user_token)
            self.assertTrue('anando\ndummy\nyuvi' in fake_out.getvalue().strip())

        #test to see following for non existent user
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowing(self.db, "bob", self.user_token)
            self.assertEquals("There is no followings with username: bob", fake_out.getvalue().strip())

        #test to see following when user is following no one
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowing(self.db, "dummy", self.user_token)
            self.assertTrue("There is no followings with username: dummy",fake_out.getvalue().strip())
        
        
    def test_ViewFollowers(self):
        #test to see followers
        # store the printed console items in the fake_out variable for assertions later
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowers(self.db, "anando", self.user_token)
            self.assertTrue('graeme' in fake_out.getvalue().strip())

        #test to see follwers for a non existent user
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowers(self.db, "bob", self.user_token)
            self.assertTrue('bob' in fake_out.getvalue().strip())

        #test to see followers when there are no followers
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ViewFollowers(self.db, "dummy", self.user_token)
            self.assertTrue('dummy' in fake_out.getvalue().strip())
        