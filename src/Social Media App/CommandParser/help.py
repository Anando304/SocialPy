## @file help.py
# @author Anando Zaman
# @brief module that displays information about available commands and their usage
# @date March 16, 2021

def help():
    instructions = '''*********************************
--------Command Reference--------
*********************************
post add [post_content]\t\t\t: Create a new post
post edit [post_id]\t\t\t: Edit post with specified ID
post delete [post_id]\t\t\t: Delete post with specified ID
    
post view followings\t\t\t: View posts of users you follow
post view\t\t\t\t: View your own posts
post view [username]\t\t\t: View specified user's posts
post view all\t\t\t\t: View all posts from all users 

profile followings_view [username]\t: View list of users you follow
profile followers_view [username]\t: View list of users that follow you
profile followings_add [username]\t: Follow a user
profile followings_delete [username]\t: Unfollow a user

profile view\t\t\t\t: View your own profile
profile view [username]\t\t\t: View profile info of specified user
profile edit_location [new_location]\t: Change your profile location
profile edit_name [new_name]\t\t: Change your profile name
profile delete account\t\t\t: Delete your account

exit\t\t\t\t\t: Exit app
help\t\t\t\t\t: Show this reference screen
clear\t\t\t\t\t: Clear the terminal screen'''
    return instructions