#  @file QueryPost.py
#  @author Anando & Yuvraj
#  @brief Used for querying/extracting posts data
#  @date Feb 20,2021

import sys
from io import StringIO

sys.path.insert(0, './')
from Profile.ViewFollowers import *

## @brief Getter method to retrieve all the posts by a given user
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents the user to query posts from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a list containing all the posts of a user
def QueryPostsByUser(db, username, user_token):
    # checks if the user exists
    checkUser = db.child('profile').child('username').child(username).get(user_token).val()
    if checkUser  == None:
        print("There is no user with the username " + username + "\n")
        return None

    # checks if the user has made any posts
    checkPost = db.child('profile').child('username').child(username).child('posts').get(user_token).val()
    if checkPost  == None or checkPost == "":
        print(username + " has no posts\n")
        return None

    # return all posts content of the user, as a set
    postContent = list(dict(checkPost.items()).values())
    return postContent

## @brief Getter method to retrieve ALL posts of the database
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a list of ALL the posts
def QueryPostsAll(db, user_token):
    posts = db.child('allposts').child('posts').get(user_token).val()
    if not posts:
        return None
    return list(posts.values())

## @brief Getter method to retrieve posts of ONLY people you are following
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param firebase: firebase object instance in order to execute commands to the Firebase console via Pyrebase API.
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a dictionary containing the posts of ALL USERS YOU FOLLOW
def QueryPostsFollowing(db, firebase, user_token):
    # retrieve your personal username
    username = firebase.get_username()

    # retrieve everyone you follow from QueryFollowers.py function
    following_list = QueryFollowing(db, username, user_token)

    # store dictionary of posts
    posts_dict = {}

    # iterate through each person you follow
    for following in following_list:
        # query all posts for that given person
        posts = QueryPostsByUser(db, following, user_token)
        # save those posts into the dictionary
        posts_dict[following] = posts
    return posts_dict

## @brief Getter method to retrieve posts of ONLY people who follow you
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param firebase: firebase object instance in order to execute commands to the Firebase console via Pyrebase API.
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @return Returns a dictionary containing the posts of ALL YOURS FOLLOWERS
def QueryPostsFollowers(db, firebase, user_token):
    # retrieve your personal username
    username = firebase.get_username()

    # retrieve everyone you follow from QueryFollowers.py function
    following_list = QueryFollowers(db, username, user_token)

    # store dictionary of posts
    posts_dict = {}

    # iterate through each person you follow
    for following in following_list:
        # query all posts for that given person
        posts = QueryPostsByUser(db, following, user_token)
        # save those posts into the dictionary
        posts_dict[following] = posts
    return posts_dict
