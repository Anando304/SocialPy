##  @file EditPost.py
#  @author Yuvraj Randhawa
#  @brief Used for editing an existing post
#  @date

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import *
from Profile.QueryProfile import *

## @brief Edit contents of an existing post, if it exists under their profile posts branch.
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param current_user: string value representing username of the user who is posting
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @param post_id: string value corresponding to the post that is to be deleted
# @details Edit the post via post_id from the allposts --> posts branch, & profile --> username --> name --> posts branch.
# @details if the post_id DOES NOT EXIST under the current_user, then prints "invalid PostID"
def EditPost(db, current_user, user_token, post_id, content):

    content = content.strip()

    validPost = db.child('profile').child('username').child(current_user).child("posts").child(post_id).get(user_token).val()

    # check if postID exists for the given user only
    if not validPost or not post_id:
        print("invalid postID")
        return

    if not content:
        print("Post content cannot be empty!")
        return

    # update the post content under the users' post branch
    db.child('profile').child('username').child(current_user).child('posts').child(post_id).update({"content": content}, user_token)
    # update the post content under the ALL Posts branch
    db.child('allposts').child('posts').child(post_id).update({"content": content}, user_token)
    print("PostID:" + post_id + ", content has been succussfully changed to: " + content)