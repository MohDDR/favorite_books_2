from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash, session
import re

class Like:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data ['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.post_id = data ['post_id']
        self.comment_id = data ['comment_id']
        self.review_id = data ['review_id']
        self.list_id = data ['list_id']
        self.liker_id = data ['liker_id']

# like or unlike review
    @classmethod
    def like_or_unlike_review(cls,review_id):
        data = { 
            'user_id' : session['user_id'],
            'review_id' : review_id
            }
        query = """
        SELECT * FROM likes
        WHERE liker_id = %(user_id)s
        && review_id = %(review_id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results == ():
            query = """
            INSERT INTO likes 
            (liker_id, review_id) 
            VALUES (%(liker_id)s, %(review_id)s)
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )
        else:
            data = {
                'id' : results[0]['id']
            }
            query = """
            DELETE FROM likes
            WHERE id = %(id)s
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )

# like or unlike comment
    @classmethod
    def like_or_unlike_comment(cls,comment_id):
        data = { 
            'user_id' : session['user_id'],
            'comment_id' : comment_id
            }
        query = """
        SELECT * FROM likes
        WHERE liker_id = %(user_id)s
        && comment_id = %(comment_id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results == ():
            query = """
            INSERT INTO likes 
            (liker_id, comment_id) 
            VALUES (%(liker_id)s, %(comment_id)s)
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )
        else:
            data = {
                'id' : results[0]['id']
            }
            query = """
            DELETE FROM likes
            WHERE id = %(id)s
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )

# like or unlike list
    @classmethod
    def like_or_unlike_list(cls,list_id):
        data = { 
            'user_id' : session['user_id'],
            'list_id' : list_id
            }
        query = """
        SELECT * FROM likes
        WHERE liker_id = %(user_id)s
        && list_id = %(list_id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results == ():
            query = """
            INSERT INTO likes 
            (liker_id, list_id) 
            VALUES (%(liker_id)s, %(list_id)s)
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )
        else:
            data = {
                'id' : results[0]['id']
            }
            query = """
            DELETE FROM likes
            WHERE id = %(id)s
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )

# like or unlike post
    @classmethod
    def like_or_unlike_post(cls,post_id):
        data = { 
            'user_id' : session['user_id'],
            'post_id' : post_id
            }
        query = """
        SELECT * FROM likes
        WHERE liker_id = %(user_id)s
        && post_id = %(post_id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results == ():
            query = """
            INSERT INTO likes 
            (liker_id, post_id) 
            VALUES (%(liker_id)s, %(post_id)s)
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )
        else:
            data = {
                'id' : results[0]['id']
            }
            query = """
            DELETE FROM likes
            WHERE id = %(id)s
            ;"""
            return connectToMySQL(cls.DB).query_db( query, data )
