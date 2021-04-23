##  @file ViewPost.py
#  @author Yuvraj
#  @brief Used for displaying posts data to the user
#  @date Feb 20,2021

import sys, math
from io import StringIO
sys.path.insert(0, './')
from Posts.QueryPosts import *

## @brief Void function that displays the posts by a given user
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents the user to query posts from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def ViewPostsByUser(db, username, user_token):
    # Query posts
    posts = QueryPostsByUser(db, username, user_token)
    if not posts:
        return

    # iterate over all posts
    print("Displaying all posts by " + username)
    for post in posts:
        printPost(post["time"], post["post_id"], post["content"], username)


## @brief Void function that displays all posts
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def ViewPostsAll(db,user_token):
    # Query posts
    posts = QueryPostsAll(db, user_token)
    if not posts:
        print("no posts to display")
        return

    print("Displaying all posts...")
    for post in posts:
        printPost(post["time"], post["post_id"], post["content"], post["username"])

## @brief  Void function that displays all posts made by the people you follow
# @param db: firebase database object instance used to execute database related commands via the Pyrebase API
# @param username: string that represents the user to query posts from
# @param user_token: string value needed to retrieve information from database in an authenticated manner
def ViewPostsFollowing(db, firebase, user_token):
    # Query posts
    query = QueryPostsFollowing(db, firebase, user_token)
    if not query or "" in query:
        print("no posts to display")
        return

    print("Displaying posts based on the the people you follow...\n")
    # iterate through each person you follow
    for following, posts in query.items():
        spacing = 55 - len(following) - 10
        lSpacing = math.ceil(spacing/2)
        rSpacing = math.floor(spacing/2)
        print('\n' + '_'*55)
        print('_'*lSpacing + 'Posts by: ' + following + '_'*rSpacing)
        print('_'*55)
        # iterate through each of the persons' post and print to the screen
        for post in posts:
            printPost(post["time"], post["post_id"], post["content"], following)

def printPost(time,post_id,content,username = ''):
    # if string has spaces split with splitContent()
    if ' ' in content:
        contentArray = splitContent(content)
    # w/o spaces just add dashes at end of line
    else:
        if len(content) > 50:
            contentArray = []
            while len(content) > 50:
                contentArray.append(content[0:49] + '-')
                content = content[49:]
            contentArray.append(content)
        else:
            contentArray = [content]

    print('\n|-----------------------------------------------------|')
    # username
    if username != '':
        usr_length = 50 - len(username)
        print('|  @' + username + ' '*usr_length + '|')
    # line break
    print('|  ' + ' '*50 + ' |')
    # content
    for line in contentArray:
        spaces = 50 - len(line)
        print('|  ' + line + ' '*spaces + ' |')
    # line break
    print('|  ' + ' '*50 + ' |')
    # time and ID
    print('|  ' + time + ' '*20 + post_id + ' |')
    print('|-----------------------------------------------------|')


def splitContent(content):
    contentArray =[]

    while len(content) > 0:
        line = content[0:50]
        nextLine = content[50:]

        # on last line break
        if nextLine == '':
            contentArray.append(line.strip())
            break

        index = -2
        char = line[-1:]
        # If last character isn't a space, scan line in
        #  reverse looking for whitespace to break on
        #  so words don't get chopped in half.
        while char != ' ':
            char = line[index : index+1]
            index -= 1

        # If while loop was run (last char wasn't a space)
        #  split the first line at index and add last
        #  word to next line.
        if index != -2:
            nextLine = line[index+1:] + nextLine
            line = line[:index+1]

        contentArray.append(line.strip())
        content = nextLine

    return contentArray
