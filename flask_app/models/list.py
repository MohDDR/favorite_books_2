from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
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

# currently reading list
# finished reading list
# users that saved this list