##  @file AddFollowers.py
#  @author Anando Zaman
#  @brief Used for adding users to the following list of the logged in user
#  @date Feb 22, 2021

import sys

sys.path.insert(0, './')
from Profile.QueryFollowers import *


## @brief Void function that updates the users' followings list
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param current_user: string that represents the current logged-in user
# @param user_to_follow: string that represents the username of the person that the current_user wants to follow
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def AddFollowers(db, current_user, user_to_follow, user_token):
    # setup
    current_user = current_user.strip().lower()
    user_to_follow = user_to_follow.strip().lower()

    # verify that you are not trying to follow yourself
    if current_user == user_to_follow:
        print("You cannot follow yourself. Please try following a valid user other than yourself.")
        return

    # prevent user from following blanks or empty spaces
    if not user_to_follow:
        print("User to follow cannot be blank. You must enter a valid username to follow")
        return

    # verify that the user that we want to follow is valid
    checkUser = db.child('profile').child('username').child(user_to_follow).get(user_token).val()
    if checkUser == None:
        print("There is no user with the username " + user_to_follow + "\n")
        return

    # query your followings list
    followings_list = set(QueryFollowing(db,current_user,user_token))
    # query user_to_follows' followers list
    followers_list = set(QueryFollowers(db,user_to_follow,user_token))

    # check if user is already in followings list to prevent duplication
    if user_to_follow in followings_list:
        print(user_to_follow + " already exists in your following list!")
        return

    # remove empty spaces if exists
    if '' in followings_list:
        followings_list.remove('')
    if '' in followers_list:
        followers_list.remove('')

    # otherwise, append the user_to_follow to your FOLLOWINGS list, and your name in the user_to_follows' FOLLOWERS list
    followings_list.add(user_to_follow)
    followers_list.add(current_user)
    followings_list = str(followings_list)[1:-1].replace("'", "").replace(" ", "")
    followers_list = str(followers_list)[1:-1].replace("'", "").replace(" ", "")


    # Push the changes to the database
    db.child("profile").child("username").child(current_user).child("following").update({"following_list": followings_list},user_token)
    db.child("profile").child("username").child(user_to_follow).child("following").update({"followers_list": followers_list}, user_token)
    print(user_to_follow + " was successfully added to your followings list!")
