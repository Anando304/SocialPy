## @file ViewFollowers.py
#  @author Anando Zaman & Yuvraj Randhawa
#  @brief Used for Display/Print Followers on to the screen
#  @date Feb 22, 2021

import sys

sys.path.insert(0, './')
from Profile.QueryFollowers import *

## @details Prints the followings list to the screen
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents username of the person to retrieve followings list from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def ViewFollowing(db, username,user_token):
    followings_list = QueryFollowing(db, username, user_token)
    if not followings_list:
        print("There is no followings with username: " + username + "\n")
        return None

    # if only one follower
    elif type(followings_list) == str:
        print("Displaying followers list for " + username + "...")
        print(followings_list)

    elif not followings_list[0]:
        print(username + " is not followings anyone" + "\n")
        return None

    else:
        print("Displaying following list for " +username + "...")
        for follower in followings_list:
            print(follower.strip())

## @details Prints the followers to the screen
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents username of the person to retrieve followings list from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def ViewFollowers(db, username,user_token):
    followers_list = QueryFollowers(db, username, user_token)
    if not followers_list:
        print("There is no followers for username: " + username + "\n")
        return None

    # if only one follower
    elif type(followers_list) == str:
        print("Displaying followers list for " + username + "...")
        print(followers_list)

    elif not followers_list[0]:
        print(username + " has no followers" + "\n")
        return None

    else:
        print("Displaying followers list for " + username + "...")
        for follower in followers_list:
            print(follower.strip())