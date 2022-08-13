from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
#from flask_bcrypt import Bcrypt        if using password ---> activate
from flask import flash
import re

class Book:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.description = data['description']
        self.page_count = data['page_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster_id = data['poster_id']

        self.reviews = []
        self.book_list = []