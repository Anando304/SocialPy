## @file CommandParser.py
# @author Anando Zaman, Graeme Woods
# @brief module used to transition control between modules
# @date March 1,2021
# @details Controller module used to parse commands/execute commands

import sys, time

sys.path.insert(0, './')
# Posts imports
from Posts.ViewPost import *
from Posts.AddPost import *
from Posts.EditPost import *
from Posts.DeletePost import *

# Profile imports
from Profile.AddFollowers import *
from Profile.DeleteFollowers import *
from Profile.ViewFollowers import *
# from Profile.DeleteAccount import *
from Profile.EditLocation import *
from Profile.EditName import *
from Profile.ViewProfile import *

# help import
from CommandParser.help import *

# import only system from os
from os import system, name

exit_text = ''' _____ _                 _           __                       _               _____            _       _______      _ 
|_   _| |               | |         / _|                     (_)             /  ___|          (_)     | | ___ \    | |
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __   _   _ ___ _ _ __   __ _  \ `--.  ___   ___ _  __ _| | |_/ /   _| |
  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | | | / __| | '_ \ / _` |  `--. \/ _ \ / __| |/ _` | |  __/ | | | |
  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | |_| \__ \ | | | | (_| | /\__/ / (_) | (__| | (_| | | |  | |_| |_|
  \_/ |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|     \__,_|___/_|_| |_|\__, | \____/ \___/ \___|_|\__,_|_\_|   \__, (_)
                                                                       __/ |                                   __/ |  
                                                                      |___/                                   |___/   '''

## @brief This class represents a the Command Parser.
# @details suite of functions that are able to parse/execute commands
class CommandParser:

    ## @brief Constructor accepts 3 parameters
    #  @param running: Boolean value that controls whole program should exit/run.
    #  @param firebase: firebase object instance to execute commands via Pyrebase API.
    #  @param db: firebase database object instance used to execute database commands
    def __init__(self,running, firebase, db):
        self.running = running
        self.firebase = firebase
        self.db = db
        self.user_token = firebase.get_user_instance()['idToken']

    ## @brief Main method used to execute the parsing of commands.
    #  @param command: string seperated by commas used to represent a command.
    def parseCommand(self,command):
        command_segments = command.strip().split()

        # command cannot be empty prompt
        if not command:
            print("Sorry, command cannot be empty! Please type 'help' to view commands.")

        # exit/help commands
        elif len(command_segments) == 1:
            if command_segments[0].lower() == 'exit':
                print(exit_text)
                self.running[0] = False
            elif command_segments[0].lower() == 'help':
                print(help())
                return
            elif command_segments[0].lower() == 'clear':
                self.clear()
                return
            else:
                print("Sorry, your command is invalid. Please type 'help' if you need to view the list of commands!")

        # parses the three command segments and executes a query to the database. Example: ['post', 'view', 'yuvi']
        else:
            # profile or post
            command_type = command_segments[0].lower()
            # view, find, delete, add, follow, edit
            command_action = command_segments[1].lower()
            # context such as post data, username, etc
            command_context = ' '.join(command_segments[2:])

            if command_type == 'post':
                self.post_commands(command_action, command_context)

            elif command_type == "profile":
                self.profile_commands(command_action, command_context.lower())

            # Incorrect command
            else:
                print("Sorry, your command is invalid. Please type 'help' if you need to view the list of commands!")



    ## @brief Main method used to execute the parsing of commands.
    # @details Parses Post commands (ex; add, view, delete) with context
    #  @param command_action: string that reps type of post command
    #  @param command_context: string that represents the context(ex; username).
    def post_commands(self,command_action, command_context):

        # Redirect to Add, delete, view commands of Posts

        if command_action == 'add':
            postContent = addPost(self.db, self.firebase.get_username(), command_context, self.user_token)
            # sleep for 2 seconds to avoid post spamming!
            time.sleep(2)
            if postContent == None:
                print("Please enter a phrase less than 200 characters!")
            else:
                print(f'Post "{postContent}" added')

        elif command_action == 'view':
            # view all posts
            if command_context == "all":
                ViewPostsAll(self.db, self.user_token)
                return
            # view posts by people you follow
            elif command_context == "followings":
                ViewPostsFollowing(self.db, self.firebase, self.user_token)
                return
            # otherwise, view posts by a specific user
            else:
                if command_context == '':
                    username = self.firebase.get_username()
                else:
                    username = command_context.lower()
                ViewPostsByUser(self.db, username, self.user_token)

        elif command_action == 'edit':
            content = input("please enter post content: ")
            post_id = command_context
            EditPost(self.db, self.firebase.get_username(), self.user_token, post_id, content)

        elif command_action == 'delete':
            DeletePost(self.db, self.firebase.get_username(), self.user_token, command_context)
            print("post deleted")
        else:
            print("Sorry, your command is invalid. Please type 'help' if you need to view the list of commands!")

    ## @brief Parses Profile commands
    # @details Parses Profile commands (ex; add, view, delete) with context
    #  @param command_action: string that represents type of profile command
    #  @param command_context: string that represents the context(ie; username).
    def profile_commands(self, command_action, command_context):

        # Redirect to Add, delete, view commands of Profile

        # Followers commands
        if command_action == 'followings_view':
            ViewFollowing(self.db, command_context, self.user_token)
        elif command_action == "followers_view":
            ViewFollowers(self.db, command_context, self.user_token)
        elif command_action == 'followings_delete':
            DeleteFollowers(self.db, self.firebase.get_username(), command_context, self.user_token)
        elif command_action == 'followings_add':
            AddFollowers(self.db, self.firebase.get_username(), command_context, self.user_token)

        # General Profile commands
        elif command_action == 'view':
            if command_context == '':
                username = self.firebase.get_username()
            else:
                username = command_context.lower()
            ViewProfile(self.db, username, self.user_token)
        elif command_action == 'edit_location':
            EditLocation(self.db, self.firebase.get_username(), self.user_token, command_context)
        elif command_action == 'edit_name':
            EditName(self.db, self.firebase.get_username(), self.user_token, command_context)
        #elif command_action == 'delete':
        #    if command_context == 'account':
        #        DeleteAccount(self.firebase, self.db, self.firebase.get_username(), self.user_token, exit_text)
        else:
            print("Sorry, your command is invalid. Please type 'help' if you need to view the list of commands!")

    ## @brief Clears the terminal after each command executes
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

        # sleep for 1 second after printing output
        time.sleep(2)



