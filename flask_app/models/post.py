from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Post:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster_id = data ['poster_id']

        self.comments = []
        self.likes = []

# create a post
    @classmethod
    def create_post(cls,data):
        query = """
        INSERT INTO posts 
        (content, poster_id) 
        VALUES (%(content)s, %(poster_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# delete a post
    @classmethod
    def delete_post(cls, post_id):
        data = { 'id' : post_id }
        query = """
        DELETE FROM posts WHERE id =%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# update a post
    @classmethod
    def update_post(cls, data):
        query = """
        UPDATE posts
        SET content = %(content)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get posts by poster id
    @classmethod
    def get_posts_by_poster(cls, poster_id):
        data = { 'id' : poster_id }
        query = """
        SELECT * FROM posts 
        WHERE poster_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        posts = []
        for post in results:
            posts.append( cls(post) )
        return posts

# get most recent posts
