from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
#from flask_bcrypt import Bcrypt        if using password ---> activate
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