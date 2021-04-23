##  @file DeleteFollowers.py
#  @author Anando Zaman
#  @brief Used for deleting followers from the following list of the logged in user
#  @date Feb 22, 2021

import sys

sys.path.insert(0, './')
from Profile.QueryFollowers import *

## @details Void function that updates the users' followings list by deleting users
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param current_user: string that represents the current logged-in user
# @param user_to_remove: string that represents the user that we want removed from followers list
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def DeleteFollowers(db, current_user, user_to_remove, user_token):
    # setup
    current_user = current_user.strip().lower()
    user_to_remove = user_to_remove.strip().lower()

    # prevent user from following blanks or empty spaces
    if not user_to_remove:
        print("User to follow cannot be blank. You must enter a valid username to remove")
        return

    # verify that the user that we want to remove exists in the system
    checkUser = db.child('profile').child('username').child(user_to_remove).get(user_token).val()
    if checkUser == None:
        print("There is no user with the username " + user_to_remove + "\n")
        return

    # query your followings list
    followings_list = set(QueryFollowing(db,current_user,user_token))
    # query user_to_follows' followers list
    followers_list = set(QueryFollowers(db,user_to_remove,user_token))

    # check if user_to_remove is in the followers_list in order to remove
    if user_to_remove not in followings_list:
        print("Sorry, " + user_to_remove + " does not exist in your following list!")
        return

    # otherwise, remove the user_to_remove from your followings list
    followings_list.remove(user_to_remove)
    followings_list = str(followings_list)[1:-1].replace("'", "").replace(" ", "") if followings_list else ""

    # remove your name from the user_to_remove's followers list since you are no longer following them
    followers_list.remove(current_user)
    followers_list = str(followers_list)[1:-1].replace("'", "").replace(" ", "") if followings_list else ""

    # Push the changes to the database
    db.child("profile").child("username").child(current_user).child("following").update({"following_list": followings_list}, user_token)
    db.child("profile").child("username").child(user_to_remove).child("following").update({"followers_list": followers_list}, user_token)
    print(user_to_remove + " was successfully removed from your followers list!")
