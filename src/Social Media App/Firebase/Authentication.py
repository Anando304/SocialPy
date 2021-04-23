##  @file Authentication.py
#  @author Anando Zaman
#  @brief Authentication module which prompts the user to login/sign_up
#  @date February 10, 2021


## @brief This class represents all that is needed to Authenticate the user.
# @details This class takes a firebase instance and db instance for the constructor
import sys, time

# help import
from CommandParser.help import *

class Authentication:
    ## @brief Constructor accepts 2 parameters
    #  @param firebase: firebase object instance in order to execute commands to the Firebase console via Pyrebase API.
    #  @param db: firebase database object instance used to execute database related commands via the Pyrebase API
    def __init__(self,firebase,db):
        self.firebase = firebase
        self.db = db
        self.timeout = 0


    ## @brief Login method
    # @details Authenticates the user credentials with that found in the Firebase console
    def login(self):
        if self.timeout >= 5:
            print("Too many failed login attempts. Please try again after 10 seconds...")
            time.sleep(10)
            self.timeout = 0

        print("Sign in - input username & password. ex; user@email.com 123456789")

        credentials = []
        while len(credentials) != 2:
            sys.stdout.write(">")
            credentials_input = input()
            credentials = credentials_input.split()
            if len(credentials) == 1 and credentials[0].lower().strip() == 'exit':
                print("Thanks for using SocialPy!")
                sys.exit()
            elif len(credentials) != 2:
                print(
                    "Invalid, please input username followed by a space followed by password. ex; user@email.com 123456789")

        if len(credentials) == 2:
            try:
                self.firebase.sign_in(credentials[0], credentials[1])

                # update local firebase username isntance field to the authenticated username
                UID = self.firebase.get_UID()
                username = self.db.child("users").child("uid").child(UID).get(self.firebase.get_user_instance()['idToken']).val()
                self.firebase.set_username(username)

                print("Login Successful!")
            except:
                print("Signin failed.")
                self.timeout += 1
                self.login()

    ## @brief Password reset
    # @details Given a valid account email, sends a reset request via email
    def password_reset(self):
        email = input("Please enter your email associated to your account: ")
        email = email.strip().split()

        # if not a valid email due to spaces!
        while len(email) != 1:
            email = input("Please enter a valid email!").strip()

        if email[0] == "exit":
            print("Thank you for using SocialPy")
            sys.exit()

        # try to send an email password reset request
        try:
            self.firebase.auth.send_password_reset_email(email[0])
            print("Password reset has been sent to your email!")
        except:
            print("Password reset failed. Please enter a valid email or type 'exit' to escape.")


    ## @brief Register method
    # @details Registers a new account provided the username and password
    def register(self):
        print("Sign up - You must be over the age of 13 to use SocialPy.")
        print("Input email followed by a space followed by password. ex; user@email.com 123456789")
        credentials = []
        while len(credentials) != 2:
            credentials_input = input()
            credentials = credentials_input.split()
            if len(credentials) == 1 and credentials[0].lower().strip() == 'exit':
                print("Thanks for using SocialPy!")
                sys.exit()
            if len(credentials) != 2:
                print(
                    "Invalid, please input email followed by a space followed by password. ex; user@email.com 123456789")

        if len(credentials) == 2:
            try:
                self.firebase.sign_up(credentials[0], credentials[1])
                print("Signup success! Please input your desired username below:")

                username = ""
                all_users = set(self.db.child("users").child("all").get(self.firebase.get_user_instance()['idToken']).val().split(","))

                # ensure username is valid
                while not username or username in all_users or username in {"all", "followings", "followers"}:
                    username = input().strip().lower()

                    # ensure username is not blank and ensure that it is not a context-command name
                    if not username or username in {"all", "followings", "followers"}:
                        print("Please enter a valid username")

                    # ensure username is not already taken
                    if username in all_users:
                        print(username, " is already taken. Please try a different username!")

                # Intialize db for the given username
                # Add to "users: --> "UID"
                self.db.child("users").child("uid").update({self.firebase.get_UID(): username},self.firebase.get_user_instance()['idToken'])

                # add to "users" --> "all" list
                all_users.add(username)
                all_users = str(all_users)[1:-1].replace("'", "").replace(" ", "")
                self.db.child("users").update({"all": all_users},self.firebase.get_user_instance()['idToken'])

                # get users name:
                name = ""
                print("Please enter your name")
                while not name:
                    name = input()
                    if not name:
                        print("please input a valid name with english characters!")

                # get users location:
                location = ""
                print("Please enter your location")
                while not location:
                    location = input()
                    if not location:
                        print("Please enter a valid location")

                # create a profile
                self.db.child("profile").child("username").child(username).update({"posts": ""},self.firebase.get_user_instance()['idToken'])
                self.db.child("profile").child("username").child(username).update({"name": name},self.firebase.get_user_instance()['idToken'])
                self.db.child("profile").child("username").child(username).update({"location": location},self.firebase.get_user_instance()['idToken'])
                self.db.child("profile").child("username").child(username).child("following").update({"following_list": ""},self.firebase.get_user_instance()['idToken'])
                self.db.child("profile").child("username").child(username).child("following").update({"followers_list": ""}, self.firebase.get_user_instance()['idToken'])

                # update local firebase username isntance field to the authenticated username
                self.firebase.set_username(username)
                print("Account profile successfully made!")
                print(help())

            except:
                print("Signup failed. Account already exists or password is not long enough")
