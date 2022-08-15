from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Message:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.recipient_id = data['recipient_id']
        self.sender_id = data['sender_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# create message

# delete message
# get user messages
# get messages sent