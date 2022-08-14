from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Friend:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.friend_username = data['friend.username']
        self.friend_email = data['friend.email']
        self.friend_created_at = data['friend.created_at']
        self.friend_updated_at = data['friend.updated_at']

# create friend relation
# remove friend relation
# text friend
# get all friends