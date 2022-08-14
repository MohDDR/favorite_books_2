from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Like:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.post_id = data ['post_id']
        self.comment_id = data ['comment_id']
        self.review_id = data ['review_id']
        self.list_id = data ['list_id']
        self.liker_id = data ['liker_id']

# like a review
# like a book
# like a comment
# like a list
# like a post
# remove a like
# get likers likes