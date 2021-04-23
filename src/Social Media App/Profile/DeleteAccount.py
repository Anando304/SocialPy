##  @file DeleteAccount.py
#  @author Anando Zaman
#  @brief Used for Deleting account from Firebase database
#  @date
# Development stage: Still in-progress

import sys
import firebase_admin
from firebase_admin import auth

sys.path.insert(0, './')
from Firebase.firebase_creds import *
from Profile.QueryProfile import *
from Posts.DeletePost import *
from Profile.QueryFollowers import *
from Profile.DeleteFollowers import *

## @brief Void function used for Deleting account from Firebase database
# @param firebase: firebase object instance in order to execute commands to the Firebase console via Pyrebase API.
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param current_user: string that represents the current logged-in user
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def DeleteAccount(firebase, db, current_user, user_token, exit_text):
    # First, remove all posts associated with account.
    profile_data = QueryProfile(db, current_user, user_token)
    FollowingList= QueryFollowing(db, current_user, user_token)

    # remove the users from following list
    if FollowingList:
        for user_to_remove in FollowingList:
            DeleteFollowers(db, current_user, user_to_remove,user_token)

    # remove current user from other peoples following list
    Followers = QueryFollowers(db, current_user, user_token)
    if Followers:
        for user in Followers:
            DeleteFollowers(db, user, current_user, user_token)


    post_id_lst = None
    try:
        post_id_lst = list(profile_data["posts"])
    except:
        post_id_lst = None

    if post_id_lst:
        for post_id in post_id_lst:
            DeletePost(db, current_user, user_token, post_id)

    # Second, Remove profile
    db.child("profile").child("username").child(current_user).remove(user_token)

    # Third, remove from users --> all branch
    all_users = set(db.child("users").child("all").get(user_token).val().split(","))
    all_users.remove(current_user)
    all_users = str(all_users)[1:-1].replace("'", "").replace(" ", "") if all_users else ""
    # push updated all users list/set to DB
    db.child("users").update({"all": all_users},user_token)

    # Fourth, remove from users --> uid branch.
    UID = firebase.get_UID().strip()
    db.child("users").child("uid").child(UID).remove(user_token)

    # Fifth, remove from authentication panel
    try:
        cred = firebase_admin.credentials.Certificate("./Firebase/socialmediaapp.json")
        firebase_admin.initialize_app(cred)
        auth.delete_user(UID)
        print("Succussfully removed account!")
        print(exit_text)
    except:
        print("Error: Failed to remove account")
    sys.exit()
