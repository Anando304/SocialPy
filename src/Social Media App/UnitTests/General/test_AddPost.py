# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class
from Posts.AddPost import addPost
from Posts.DeletePost import DeletePost


class TestAddPost(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def test_AddPost(self):
        # test to add a short post
        addPost(self.db, "dummy", "Testing post", self.user_token)
        userPosts = self.db.child('profile').child('username').child("dummy").child("posts").get(self.user_token)
        newPost = userPosts[len(userPosts.each()) - 1].val()
        self.assertEqual(newPost["content"], "Testing post")

        # test to add a post that is too long
        string_215_chars = "This is a really long post This is a really long post This is a really long post This is a really long post This is a really long post This is a really long post This is a really long post This is a really long post"

        postResponse = addPost(self.db, "dummy", string_215_chars, self.user_token)
        self.assertEqual(postResponse, None)


        # delete test post
        DeletePost(self.db, "dummy", self.user_token, newPost["post_id"])





