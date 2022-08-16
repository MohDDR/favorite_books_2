from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Comment:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.commenter_id = data['commenter_id']
        self.post_id = data['post_id']
        self.list_id = data['list_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.likes = []

# create a post comment
    @classmethod
    def create_post_comment(cls,data):
        query = """
        INSERT INTO comments 
        (content, commenter_id, post_id) 
        VALUES (%(content)s, %(commenter_id)s, %(post_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# create a list comment
    @classmethod
    def create_list_comment(cls,data):
        query = """
        INSERT INTO comments 
        (content, commenter_id, list_id) 
        VALUES (%(content)s, %(commenter_id)s, %(list_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# edit a comment
    @classmethod
    def update_post_comment(cls, data):
        query = """
        UPDATE comments
        SET content = %(content)s, commenter_id = %(commenter_id)s, 
        post_id = %(post_id)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# edit a comment
    @classmethod
    def update_list_comment(cls, data):
        query = """
        UPDATE comments
        SET content = %(content)s, commenter_id = %(commenter_id)s, 
        list_id = %(list_id)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# delete a comment
    @classmethod
    def delete_comment(cls, comment_id):
        data = { 'id' : comment_id }
        query = """
        DELETE FROM comments WHERE id =%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get comments by post
    @classmethod
    def get_comments_by_post(cls, post_id):
        data = { 'id' : post_id }
        query = """
        SELECT * FROM comments 
        WHERE post_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        comments = []
        for comment in results:
            comments.append( cls(comment) )
        return comments

# get comments by list
    @classmethod
    def get_comments_by_list(cls, list_id):
        data = { 'id' : list_id }
        query = """
        SELECT * FROM comments 
        WHERE list_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        comments = []
        for comment in results:
            comments.append( cls(comment) )
        return comments

# get comments by commenter
    @classmethod
    def get_comments_by_commenter(cls, commenter_id):
        data = { 'id' : commenter_id }
        query = """
        SELECT * FROM comments 
        WHERE commenter_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        comments = []
        for comment in results:
            comments.append( cls(comment) )
        return comments
