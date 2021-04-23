##  @file DeletePost.py
#  @author Yuvraj Randhawa
#  @brief Used for Deleting a post
#  @date

import sys

sys.path.insert(0, './')
from Firebase.firebase_creds import *
from Profile.QueryProfile import *

## @brief Delete a current logged-in users' post by post_id, if exists.
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param current_user: string value representing username of the user who is posting
# @param user_token: string value needed to retrieve information from database in an authenticated manner
# @param post_id: string value corresponding to the post that is to be deleted
# @details Removes the post via post_id from the allposts --> posts branch, & profile --> username --> name --> posts branch
def DeletePost(db, current_user, user_token, post_id):

    try:
        # check if valid post under the current users branch
        validPost = db.child('profile').child('username').child(current_user).child("posts").child(post_id).get(user_token).val()
        if not validPost or not post_id:
            print("invalid postID")
            return

        else:
            # Remove post from allposts
            db.child("allposts").child("posts").child(post_id).remove(user_token)
            # Remove post from user profile
            db.child("profile").child("username").child(current_user).child("posts").child(post_id).remove(user_token)
    except:
        print("An exception has occurred. Please try again with a valid PostID")
