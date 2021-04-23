##  @file ViewProfile.py
#  @author Graeme Woods
#  @brief Used for displaying/printing profile information to the screen in a formatted way
#  @date

import sys

sys.path.insert(0, './')
from Profile.QueryProfile import *

## @details Prints the Profile information to the console in a formatted way
#  @param db: tales the database object instance
#  @param username: takes the username as a string
#  @param user_token: takes the token string for authenticated data retrieval purposes
#  @return None
def ViewProfile(db, username, user_token):

    profile = QueryProfile(db, username, user_token)
    if profile == None:
        print("Sorry, profile for the given username does not exist")
        return
    else:
        print("----"+profile["name"]+"----")
        print("Location: "+profile["location"])

        followers_list = profile["following"]["followers_list"].split(",")
        print("Followers List: ")
        if followers_list[0] != "":
            for follower in followers_list:
                print("- "+follower)
        else:
            print(profile["name"]+" has no followers.")

        following_list = profile["following"]["following_list"].split(",")
        print("Following List: ")
        if following_list[0] != "":
            for following in following_list:
                print("- "+following)
        else:
            print(profile["name"]+" is not following anyone.")

