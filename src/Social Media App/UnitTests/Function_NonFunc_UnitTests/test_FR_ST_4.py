# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class FR_ST_4(TestCase):

    def setUp(self):
        # Create connection to DB
        self.firebase = firebase_class()
        self.firebase.sign_in("dummy@gmail.com", "123456789")
        self.firebase.set_username("dummy")
        self.user_token = self.firebase.get_user_instance()['idToken']
        # Get database instance
        self.db = self.firebase.get_db()

    def testCommandParser(self):
        running = [True]
        command_parser = CommandParser(running, self.firebase, self.db)
        with mock.patch('Posts.ViewPost.QueryPostsByUser', return_value=[{'content': "Anakin, you're going down a path i cannot follow.",
                                                                          'post_id': '-MWIr7MbPHHpcrl-5ca0',
                                                                          'time': '03/21/2021'},
                                                                         {'content': 'Execute Order 66',
                                                                          'post_id': '-MWIrOezXVoDC--zkVBq',
                                                                          'time': '03/21/2021'}
                                                                         ]), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            command_parser.parseCommand("post view dummy")
            self.assertTrue('''|-----------------------------------------------------|
|  @dummy                                             |
|                                                     |
|  Anakin, you're going down a path i cannot follow.  |
|                                                     |
|  03/21/2021                    -MWIr7MbPHHpcrl-5ca0 |
|-----------------------------------------------------|

|-----------------------------------------------------|
|  @dummy                                             |
|                                                     |
|  Execute Order 66                                   |
|                                                     |
|  03/21/2021                    -MWIrOezXVoDC--zkVBq |
|-----------------------------------------------------|''' in fake_out.getvalue().strip())