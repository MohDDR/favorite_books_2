from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask_app.models import user
from flask import flash, session
import re

class List:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book_id = data['book_id']
        self.creator_id = data['creator_id']

        self.likes = []
        self.users_who_saved = []

# create a list
    @classmethod
    def create_list(cls,data):
        query = """
        INSERT INTO book_lists 
        (title, description, book_id, creator_id) 
        VALUES (%(title)s, %(description)s, %(book_id)s, %(creator_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# delete a list
    @classmethod
    def delete_list(cls, list_id):
        data = { 'id' : list_id }
        query = """
        DELETE FROM book_lists WHERE id =%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# update a list
    @classmethod
    def update_list(cls, data):
        query = """
        UPDATE book_lists
        SET title = %(title)s, description = %(description)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get list by id with the users who saved it
    @classmethod
    def get_list_with_users_who_saved(cls, list_id):
        data = { 'id' : list_id }
        query = """
        SELECT * FROM book_lists 
        LEFT JOIN saved_lists ON saved_lists.list_id = book_lists.id 
        LEFT JOIN users ON saved_lists.user_id = users.id 
        WHERE book_lists.id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        list = cls( results[0] )
        for row in results:
            user_data = {
                'id' : row['users.id'],
                'username' : row['username'],
                'email' : row['email'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            list.users_who_saved.append( user.User( user_data ) )
        return list

# get lists by creator id
    @classmethod
    def get_all_lists_by_creator_id(cls, creator_id):
        data = { 'id' : creator_id }
        query = """
        SELECT * FROM book_lists 
        WHERE creator_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        book_lists = []
        for book_list in results:
            book_lists.append( cls(book_list) )
        return book_lists

# get lists by book id
    @classmethod
    def get_all_lists_by_book_id(cls, book_id):
        data = { 'id' : book_id }
        query = """
        SELECT * FROM book_lists 
        WHERE book_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        book_lists = []
        for book_list in results:
            book_lists.append( cls(book_list) )
        return book_lists

# save list
    @classmethod
    def save_list(cls,data):
        query = """
        INSERT INTO saved_lists
        (user_id, list_id)
        VALUES (%(user_id)s, %(list_id)s)
        :"""
        connectToMySQL(cls.DB).query_db(query, data)

# lists saved by user
    @classmethod
    def get_users_saved_lists(cls):
        data = { 'id' : session['user_id']}
        query = """
        SELECT * FROM saved_lists
        WHERE user_id = %(id)s
        :"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        saved_lists = []
        for book_list in results:
            saved_lists.append( cls(book_list) )
        return saved_lists