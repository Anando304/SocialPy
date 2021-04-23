##  @file EditName.py
#  @author Yuvraj Randhawa
#  @brief Used for Updating Profile Name information of the logged in user
#  @date

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import *
from Profile.QueryProfile import *

## @brief Update Profile name information
# @details if new_name is empty or None, display error message
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents the current logged-in user
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @param new_name: string used for updating old name to new name
def EditName(db, username, user_token, new_name):

    new_name = new_name.strip()
    if not new_name:
        print("Name field cannot be empty...")
        return

    db.child('profile').child('username').child(username).update({"name": new_name}, user_token)
    name = db.child('profile').child('username').child(username).child('name').get(user_token).val()
  
    print("Name has been set to "+name)