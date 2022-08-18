from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Book:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.genre = data['genre']
        self.description = data['description']
        self.page_count = data['page_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster_id = data['poster_id']

        self.reviews = []
        self.lists = []

# add a book
    @classmethod
    def create_book(cls,data):
        query = """
        INSERT INTO books 
        (title, author, description, page_count, poster_id, genre) 
        VALUES (%(title)s, %(author)s, %(description)s, 
        %(page_count)s, %(poster_id)s, %(genre)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# edit a book
    @classmethod
    def update_book(cls, data):
        query = """
        UPDATE books
        SET title = %(title)s, author = %(author)s, 
        description = %(description)s, page_count = %(page_count)s,
        poster_id = %(poster_id)s, genre = %(genre)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# delete a book
    @classmethod
    def delete_book(cls, book_id):
        data = { 'id' : book_id }
        query = """
        DELETE FROM books WHERE id =%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get book by title
    @classmethod
    def get_books_by_title(cls, title):
        data = { 'title' : title }
        query = """
        SELECT * FROM books 
        WHERE title OR author OR genre LIKE "%(title)s"
        ;""" 
        #search item requires % at start and end, and replaces all spaces
        results = connectToMySQL(cls.DB).query_db( query, data )
        books = []
        for book in results:
            books.append( cls(book) )
        return books

# get book by author
    @classmethod
    def find_books_by_poster(cls, poster_id):
        data = { 'id' : poster_id }
        query = """
        SELECT * FROM books 
        WHERE poster_id = %(id)s
        ;""" 
        results = connectToMySQL(cls.DB).query_db( query, data )
        books = []
        for book in results:
            books.append( cls(book) )
        return books

# get book by description keyword
    @classmethod
    def find_books_by_desc(cls, desc):
        data = { 'desc' : desc }
        query = """
        SELECT * FROM books 
        WHERE description LIKE "%(desc)s"
        ;""" 
        #search item requires % at start and end, and replaces all spaces
        results = connectToMySQL(cls.DB).query_db( query, data )
        books = []
        for book in results:
            books.append( cls(book) )
        return books

# get book by id
    @classmethod
    def get_book_by_id(cls, book_id):
        data = { 'id' : book_id }
        query = """
        SELECT * FROM books 
        LEFT JOIN reviews ON reviews.book_id = books.id
        LEFT JOIN book_lists ON book_lists.book_id = books.id 
        WHERE books.id = %(id)s
        ;""" 
        results = connectToMySQL(cls.DB).query_db( query, data )
        book_with_reviews_and_lists = cls( results[0] )
        for row in results:
            this_book_reviews = {
                "id": row['reviews.id'], 
                "rating": row['rating'],
                "content": row['content'],
                "book_id": row['book_id'],
                "reviewer_id": row['reviewer_id'],
                "created_at": row['reviews.created_at'],
                "updated_at": row['reviews.updated_at']
            }
            this_book_lists = {
                "id": row['book_lists.id'], 
                "title": row['book_lists.title'],
                "description": row['description'],
                "book_id": row['book_lists.book_id'],
                "creator_id": row['creator_id'],
                "created_at": row['book_lists.created_at'],
                "updated_at": row['book_lists.updated_at']
            }
            book_with_reviews_and_lists.reviews = this_book_reviews
            book_with_reviews_and_lists.lists = this_book_lists
        return book_with_reviews_and_lists