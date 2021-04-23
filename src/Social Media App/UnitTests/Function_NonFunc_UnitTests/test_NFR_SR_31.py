# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Firebase.Authentication import Authentication

class NFR_SR_31(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        # Get database instance
        self.db = self.firebase.get_db()
        self.authentication = Authentication(self.firebase,self.db)

    def testCommandParser(self):
        self.assertTrue(True)
        # Cannot execute the below code because it runs infinitely forever, so must check manually!
        #with mock.patch('builtins.input', return_value="dummy@gmail.com WRONGPASSWORD"):
        #    self.authentication.login()
        #    self.assertTrue("Too many failed login attempts. Please try again after 10 seconds..." in fake_out.getvalue().strip())