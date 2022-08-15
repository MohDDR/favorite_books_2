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

        self.sender = None

# create message
    @classmethod
    def create_message(cls,data):
        query = """
        INSERT INTO messages 
        (content, recipient_id, sender_id) 
        VALUES (%(content)s, %(recipient_id)s, %(sender_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# delete message
    @classmethod
    def delete_message(cls, message_id):
        data = { 'id' : message_id }
        # create authorizations
        query = """
        DELETE FROM messages WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get user messages user has sent and received
    @classmethod
    def get_user_messages(cls, user_id):
        data = { 'id' : user_id }
        query = """
        "select messages.*,
        sender.id, sender.username from users as sender
        left join messages on messages.sender_id = sender.id
        left join users as recipient on messages.recipient_id = recipient.id
        where recipient.id or sender.id = %(id)s
        ; """
        results = connectToMySQL(cls.DB).query_db( query, data )
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages
