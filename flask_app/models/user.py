from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import datetime
#from flask_bcrypt import Bcrypt        if using password ---> activate
from flask import flash
import re

#bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.books_reviewed = []
        self.books_posted = []
        self.users_book_lists = []
        self.friends = []
        self.posts = []
        self.likes = []

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)

    @staticmethod
    def validate_what( data ):
        is_valid = True
        if not EMAIL_REGEX.match(data['?']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

