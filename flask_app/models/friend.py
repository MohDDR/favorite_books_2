from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask_app.models import user
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

        self.relations = []

# look for existing relation
    @staticmethod
    def check_for_relation(data):
        query = """
        SELECT * FROM friends
        WHERE user_id = %(user_id)s
        && friend_id = %(friend_id)s
        ;"""
        results = connectToMySQL(Friend.DB).query_db(query, data)
        if results == ():
            return False
        else:
            return True

# create friend relation
    @classmethod
    def create_friend_relation(cls, data):
        if not Friend.check_for_relation():
            query = """
            INSERT INTO friends 
            ( user_id, friend_id ) 
            VALUES ( %(user_id)s, %(friend_id)s )
            ;"""
            connectToMySQL(cls.DB).query_db( query, data )

# remove friend relation
    @classmethod
    def delete_friend_relation(cls, data):
        if Friend.check_for_relation():
            query = """
            DELETE FROM friends 
            WHERE friend_id = %(friend_id)s,
            && user_id = %(user_id)s
            ;"""
            connectToMySQL(cls.DB).query_db( query, data )

# get user friends
    @classmethod
    def get_user_friends(cls, data):
        query = """
        SELECT * FROM friends
        LEFT JOIN users ON friends.user_id = user.id
        LEFT JOIN users AS friend ON friends.friend_id = friend.id
        WHERE friends.user_id = %(user_id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query)
        user_friends = []
        for row in results:
            friend_data = {
                "friend_id" : row["friend.id"],
                "friend_username" : row["friend.username"],
                "friend_email" : row["friend.email"],
                "friend_created_at" : row["friend.created_at"],
                "friend_updated_at" : row["friend.updated_at"],
            }
            user_data = {
                "id" : row["user.id"],
                "username" : row["user.username"],
                "email" : row["user.email"],
                "created_at" : row["user.created_at"],
                "updated_at" : row["user.updated_at"],
            }
            print('user_friends ************** ',( user_data ), (friend_data))
            user_friends.append( user.User( user_data ), cls(friend_data) )
        print('user_friends ************** ',user_friends)
        return user_friends