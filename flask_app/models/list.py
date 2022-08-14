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
        self.book_list = []

# create a list
# delete a list
# edit a list
# get lists by creator id
# get lists by book id
# get all lists