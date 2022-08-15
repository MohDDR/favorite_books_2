from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
from flask import flash
import re

class Review:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.rating = data['rating']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book_id = data['book_id']
        self.reviewer_id = data['reviewer_id']

        self.likes = []
        self.reviewer = None
        self.book = None

# create a review
    @classmethod
    def create_review(cls,data):
        query = """
        INSERT INTO reviews 
        (rating, content, book_id, reviewer_id) 
        VALUES (%(rating)s, %(content)s, %(book_id)s, %(reviewer_id)s)
        ;"""
        connectToMySQL(cls.DB).query_db(query, data)

# delete a review
    @classmethod
    def delete_review(cls, review_id):
        data = { 'id' : review_id }
        query = """
        DELETE FROM reviews WHERE id =%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# update a review
    @classmethod
    def update_review(cls, data):
        query = """
        UPDATE reviews
        SET rating = %(rating)s, content = %(content)s, 
        book_id = %(book_id)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db( query, data )

# get reviews by book id
    @classmethod
    def get_all_reviews_by_book_id(cls, book_id):
        data = { 'id' : book_id }
        query = """
        SELECT * FROM reviews 
        WHERE book_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        reviews = []
        for review in results:
            reviews.append( cls(review) )
        return reviews

# get reviews by reviewer id
    @classmethod
    def get_all_reviews_by_reviewer_id(cls, reviewer_id):
        data = { 'id' : reviewer_id }
        query = """
        SELECT * FROM reviews 
        WHERE reviewer_id = %(id)s
        ;"""
        results = connectToMySQL(cls.DB).query_db( query, data )
        reviews = []
        for review in results:
            reviews.append( cls(review) )
        return reviews
