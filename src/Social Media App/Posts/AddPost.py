##  @file AddPost.py
#  @author Graeme Woods
#  @brief Used for addingPosts by the specified user
#  @details This is a standalone function just for POC purposes. It will later be incorporated into a class for Posts
#  @date Feb 21, 2021

import datetime
import sys
sys.path.insert(0, './')
from Firebase.firebase_creds import firebase_class

## @brief Adds a Post with at most 100 characters, for a valid username
#  @param db: firebase database object instance used to execute database related commands via the Pyrebase API
#  @param username: string value representing username of the user who is posting
#  @param content: string value representing the users' post content
#  @param user_token: string value needed to retrieve information from database in an authenticated manner
#  @return Returns the post that was added.
def addPost(db, username, content, user_token):

    if content == None or len(content) > 200:
        return None

    data = {
        "time": datetime.datetime.now().strftime("%m/%d/%Y"),
        "content": content,
        "post_id": ""
    }

    # push the post to the profile --> posts section
    push_data = db.child("profile").child("username").child(username).child("posts").push(data,user_token)

    # extract post_id after pushing
    post_id = push_data['name']

    # append the post_id into the post data
    db.child("profile").child("username").child(username).child("posts").child(post_id).update({"post_id": post_id},user_token)

    # ALLPOSTS - Duplicate the data for the allposts section
    query_data = data
    query_data["post_id"] = post_id
    query_data['username'] = username
    db.child("allposts").child("posts").child(post_id).set(query_data,user_token)

    return db.child("profile").child("username").child(username).child("posts").child(post_id).get(user_token).val()["content"]