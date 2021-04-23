# imports for testing
from unittest import TestCase, mock
import sys
# import for reading printed input and saving to a variable!
from io import StringIO

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

from CommandParser.CommandParser import *

class FR_ST_1(TestCase):

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
        with mock.patch('Posts.ViewPost.QueryPostsAll', return_value=[{'username': "anando",
                                                                          'post_id': '-MWIpcZlD7vuC4oybA4G',
                                                                          'time': '03/21/2021',
                                                                       "content": "Hey! I am Anando Zaman"},
                                                                         {'username': "anando",
                                                                          'post_id': '-MWIpnMbZaY0_gv7vZAN',
                                                                          'time': '03/21/2021',
                                                                       "content": "anakin my allegiance is to the republic to democracy!"},
                                                                         {'username': "graeme",
                                                                          'post_id': '-MWIqFLWUCDvujKJ_26G',
                                                                          'time': '03/21/2021',
                                                                       "content": "I have brought peace, freedom, justice, and security to my new empire."},
                                                                         {'username': "graeme",
                                                                          'post_id': '-MWIqRbZAAa5HKFC4_qj',
                                                                          'time': '03/21/2021',
                                                                       "content": "Star Wars: Episode III - Revenge of the Sith"},
                                                                         {'username': "yuvi",
                                                                          'post_id': '-MWIrOezXVoDC--zkVBq',
                                                                          'time': '03/21/2021',
                                                                       "content": "Execute Order 66"}
                                                                         ]), mock.patch('sys.stdout', new=StringIO()) as fake_out:
            command_parser = CommandParser(running, self.firebase, self.db)
            command_parser.parseCommand("post view all")
            self.assertTrue('''|-----------------------------------------------------|
|  @anando                                            |
|                                                     |
|  Hey! I am Anando Zaman                             |
|                                                     |
|  03/21/2021                    -MWIpcZlD7vuC4oybA4G |
|-----------------------------------------------------|

|-----------------------------------------------------|
|  @anando                                            |
|                                                     |
|  anakin my allegiance is to the republic to         |
|  democracy!                                         |
|                                                     |
|  03/21/2021                    -MWIpnMbZaY0_gv7vZAN |
|-----------------------------------------------------|

|-----------------------------------------------------|
|  @graeme                                            |
|                                                     |
|  I have brought peace, freedom, justice, and        |
|  security to my new empire.                         |
|                                                     |
|  03/21/2021                    -MWIqFLWUCDvujKJ_26G |
|-----------------------------------------------------|

|-----------------------------------------------------|
|  @graeme                                            |
|                                                     |
|  Star Wars: Episode III - Revenge of the Sith       |
|                                                     |
|  03/21/2021                    -MWIqRbZAAa5HKFC4_qj |
|-----------------------------------------------------|

|-----------------------------------------------------|
|  @yuvi                                              |
|                                                     |
|  Execute Order 66                                   |
|                                                     |
|  03/21/2021                    -MWIrOezXVoDC--zkVBq |
|-----------------------------------------------------|''' in fake_out.getvalue().strip())
