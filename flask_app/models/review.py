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
        self.book_id = data['book']
        self.reviewer_id = data['reviewer']

        self.likes = []

# create a review
# delete a review
# edit a review
# get all reviews
# get reviews by book id
# get reviews by reviewer id
