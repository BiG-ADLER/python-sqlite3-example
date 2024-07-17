# add sqlite library to project
from sqlite3 import connect

# create Connect variable and connect project to database
Connect = connect('users.db')

# create database cursor
Cursor = Connect.cursor()

# create users table if not exists
Cursor.execute("CREATE TABLE IF NOT EXISTS users(first_name, last_name, username, password)")


class Database:
    def __init__(self, username):
        self.username = username

    def checkCreationStatus(self):
        return Cursor.execute(f"SELECT * FROM users WHERE username='{self.username}'").fetchone()

    # create user
    @staticmethod
    def create(firstName, lastName, username, password):

        # add user data into users table
        Cursor.execute(f"INSERT INTO users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)", (firstName, lastName, username, password))

        # save added data in users table
        Connect.commit()

        # get saved data from database
        userData = Cursor.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()

        # return saved data from database
        return {
            'fname': userData[userData.index(firstName)],
            'lname': userData[userData.index(lastName)],
            'username': userData[userData.index(username)],
            'password': userData[userData.index(password)]
        }

    # login into user account and return to user
    @staticmethod
    def login(username, password):
        # get saved data from database
        userData = Cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'").fetchone()

        # return saved data from database
        return {
            'fname': userData[0],
            'lname': userData[1],
            'username': userData[2]
        }