from email import message
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash, session
import re
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    DB = 'favorite_books_schema'

    def __init__( self , data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.books_reviewed = []
        self.books_posted = []
        self.users_saved_lists = []
        self.friends = []
        self.posts = []
        self.likes = []
        self.messages_received = []
        self.messages_sent = []

    @classmethod
    def login(cls, data):
        query = """
        SELECT * FROM users 
        WHERE email = %(email)s
        ;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        user = cls( results[0] )
        session['user_id'] = user.id

    @classmethod
    def register(cls,data):
        query = """
        INSERT INTO users 
        (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        ;"""
        session['user_id'] = connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_user_by_id(cls):
        data = { 'id' : session['user_id']}
        query = '''
        SELECT * FROM users
        WHERE id = %(id)s
        ;'''
        results = connectToMySQL(User.DB).query_db(query, data)
        user = cls( results[0] )
        return user

# get user with messages
    @classmethod
    def get_user_with_messages(cls):
        data = { 'id' : session['user_id']}
        query = '''
        SELECT * FROM messages
        LEFT JOIN users AS sender ON messages.sender_id = sender.id
        LEFT JOIN users AS recipient ON messages.recipient_id = recipient.id
        WHERE recipient.id = %(id)s
        ;'''
        results = connectToMySQL(User.DB).query_db(query, data)
        user_with_messages = []
        for row in results:
            user_with_messages = cls(row)
            messages = {
                "id" : row["messages.id"],
                "content" : row['content'],
                "sender_id" : row['sender_id'],
                "recipient_id" : row['recipient_id'],
                "created_at" : row["messages.created_at"],
                "updated_at" : row["messages.updated_at"],
            }
            print('friendship ************** ',( user_with_messages ), (messages))
            # needs editing
            user_with_messages.messages_received.append( message.Message( messages ))
            user_with_messages.messages_sent.append( message.Message( messages ))
        return user_with_messages

# get messages user sent

# get most recent user activity

# get user with saved lists, posts, friends

    @staticmethod
    def get_user_by_email(data):
        query = '''
        SELECT * FROM users
        WHERE email = %(email)s
        ;'''
        results = connectToMySQL(User.DB).query_db(query, data)
        return results

    @staticmethod
    def validate_registration_form( data ):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']): #| User.email_search(data): 
            flash("Invalid email address!")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("first name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.")
            is_valid = False
        if User.get_user_by_email(data):
            flash("Invalid email address!")
            is_valid = False
        if len(data['password']) < 8:
            flash("password must be at least 8 characters.")
            is_valid = False
        if bcrypt.check_password_hash(data['password'], data['password']):
            flash("your passwords are not the same!!!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login_form( data ):
        is_valid = False
        if User.email_search(data):
            user = User.email_search(data)
            password = user[0]['password']
            if bcrypt.check_password_hash(password, data['password']):
                is_valid = True
        flash("Invalid login information!")
        return is_valid

    @staticmethod
    def parse_registration_data(data):
        parsed_data = {
            'first_name' : data['first_name'],
            'last_name' : data['last_name'],
            'email' : data['email'].lower(),
            'password' :  bcrypt.generate_password_hash(data['password'])
        }
        return parsed_data

    @staticmethod
    def parse_login_data(data):
        parsed_data = {
            'email' : data['email'].lower(),
            'password' : data['password']
        }
        return parsed_data