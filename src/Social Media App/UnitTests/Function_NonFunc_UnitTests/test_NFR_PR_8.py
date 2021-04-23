# imports for testing
from unittest import TestCase, mock
import sys, time
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from Firebase.Authentication import Authentication

class NFR_PR_8(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        # Get database instance
        self.db = self.firebase.get_db()
        self.authentication = Authentication(self.firebase,self.db)

    def testCommandParser(self):

        # Test 1: Login with valid credentials
        with mock.patch('builtins.input', return_value="dummy@gmail.com 123456789"):
            start = time.time()
            self.authentication.login()
            self.assertTrue(time.time()-start <= 4)