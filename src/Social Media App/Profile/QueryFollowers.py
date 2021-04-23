## @file QueryFollowers.py
#  @author Anando Zaman
#  @brief Used for Querying Followers list from the database
#  @date Feb 22, 2021

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class


## @brief Getter method to query a persons' following list.
# @details if username does not exist, return None, otherwise returns the following-list.
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents username of the person to retrieve following list from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a list of users the person is following. If invalid user, return None
def QueryFollowing(db, username,user_token):
    #checks if the user exists
    checkUser = db.child('profile').child('username').child(username).get(user_token).val()
    if checkUser == None:
        return None

    # Otherwise, retrieve the followers
    followings_list = db.child("profile").child("username").child(username).child("following").child("following_list").get(user_token).val()
    if followings_list:
        followings_list = followings_list.split(",")
    return followings_list


## @brief Getter method to query a persons' followers list.
# @details if username does not exist, return None, otherwise returns the followers-list.
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents username of the person to retrieve followers list from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a list of users followers. If invalid user, return None
def QueryFollowers(db, username,user_token):
    #checks if the user exists
    checkUser = db.child('profile').child('username').child(username).get(user_token).val()
    if checkUser == None:
        return None

    # Otherwise, retrieve the followers
    followers_list = db.child("profile").child("username").child(username).child("following").child("followers_list").get(user_token).val()
    if followers_list:
        followers_list = followers_list.split(",")
    return followers_list