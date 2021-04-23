##  @file QueryProfile.py
#  @author Anando Zaman
#  @brief Used for querying data for profile from Firebase
#  @date Feb 26,2021

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import *

## @brief Returns a dictionary containing information about a users' profile(if exists), otherwise None
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents username of the person to retrieve profile info from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def QueryProfile(db, username, user_token):
    # checks if the user exists
    profile = db.child('profile').child('username').child(username).get(user_token).val()
    if profile == None:
        print("There is no user with the username " + username + "\n")
        return None

    return dict(profile)