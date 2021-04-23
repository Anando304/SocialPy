# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO
from datetime import datetime

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.QueryPosts import QueryPostsByUser
from Profile.QueryProfile import QueryProfile

class NFR_PR_7(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_NFR_PR_7(self):
        # time queries to the database
        before1 = datetime.now()
        QueryPostsByUser(self.db,"dummy",self.user_token)
        after1 = datetime.now()

        query1_time = after1 - before1

        self.assertLessEqual(query1_time.seconds, 2)

        before2 = datetime.now()
        QueryProfile(self.db,"dummy",self.user_token)
        after2 = datetime.now()

        query2_time = after2 - before2

        self.assertLessEqual(query2_time.seconds, 2)
