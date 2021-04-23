# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class FR_ST_10(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def testCommandParser(self):
        # test help

        running = [True]
        command_parser = CommandParser(running, self.firebase, self.db)

        help_output = '''*********************************
--------Command Reference--------
*********************************
post add [post_content]\t\t\t: Create a new post
post edit [post_id]\t\t\t: Edit post with specified ID
post delete [post_id]\t\t\t: Delete post with specified ID
    
post view followings\t\t\t: View posts of users you follow
post view\t\t\t\t: View your own posts
post view [username]\t\t\t: View specified user's posts
post view all\t\t\t\t: View all posts from all users 

profile followings_view [username]\t: View list of users you follow
profile followers_view [username]\t: View list of users that follow you
profile followings_add [username]\t: Follow a user
profile followings_delete [username]\t: Unfollow a user

profile view\t\t\t\t: View your own profile
profile view [username]\t\t\t: View profile info of specified user
profile edit_location [new_location]\t: Change your profile location
profile edit_name [new_name]\t\t: Change your profile name
profile delete account\t\t\t: Delete your account

exit\t\t\t\t\t: Exit app
help\t\t\t\t\t: Show this reference screen
clear\t\t\t\t\t: Clear the terminal screen'''

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            command_parser.parseCommand("help")
            self.assertEqual(fake_out.getvalue().strip(),help_output)