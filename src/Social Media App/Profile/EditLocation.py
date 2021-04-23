##  @file EditLocation.py
#  @author Graeme Woods
#  @brief Used for Updating Profile location information of the logged in user
#  @date

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import *
from Profile.QueryProfile import *

## @brief Update profile location information
# @details if new_location parameter is empty or None, display error message
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents the current logged-in user
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @param new_location: string that represents the location that is to be used to update
def EditLocation(db, username, user_token, new_location):

    new_location = new_location.strip()
    if not new_location:
        print("Location field cannot be empty...")
        return

    db.child('profile').child('username').child(username).update({"location": new_location}, user_token)
    location = db.child('profile').child('username').child(username).child('location').get(user_token).val()

    print("Location has been set to "+location)