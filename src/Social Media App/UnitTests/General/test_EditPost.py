# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO


sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.EditPost import EditPost

class TestEditPost(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_EditPost(self):
        #test to edit a post
        EditPost(self.db, "dummy", self.user_token, "-MX9b5LJv5nK5oweH39e", "Updated Post")
        UpdatedPost = self.db.child('profile').child('username').child("dummy").child("posts").child("-MX9b5LJv5nK5oweH39e").child('content').get(self.user_token).val()
        self.assertEqual(UpdatedPost,"Updated Post")

        #test to edit a non existing post
        EditPost(self.db, "dummy", self.user_token, "W", "Updated Post")
        UpdatedPost = self.db.child('profile').child('username').child("dummy").child("posts").child("W").child('content').get(self.user_token).val()
        print(UpdatedPost)
        self.assertEqual(UpdatedPost,None)
        
        #test to edit a post with no updated post content
        BeforeChange = self.db.child('profile').child('username').child("dummy").child("posts").child("-MX9b5LJv5nK5oweH39e").child('content').get(self.user_token).val()
        EditPost(self.db, "dummy", self.user_token, "-MX9b5LJv5nK5oweH39e", " ")
        UpdatedPost = self.db.child('profile').child('username').child("dummy").child("posts").child("-MX9b5LJv5nK5oweH39e").child('content').get(self.user_token).val()
        self.assertEqual(BeforeChange, UpdatedPost)


        
