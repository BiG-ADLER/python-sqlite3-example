# import database handler
from .Database import Database


class Init:

    @staticmethod
    def run():

        # get username from user
        username = input("Please Enter your Username: ")

        # initialize Database class
        UserData = Database(username)
        # check that entered username in cmd, exits in database or not
        if UserData.checkCreationStatus() == None:
            ### if username not exists in database, then call @static(create) method in Database and create user in database

            # get user first name
            first_name = input("Please Enter your First name: ")

            # get user last name
            last_name = input("Please Enter your Last name: ")

            # get user password
            password = input("Please Enter your Password: ")

            # create and save user to database
            createdUser = Database.create(first_name, last_name, username, password)

            print(f'hello dear {createdUser['fname']}, here is your information,\nFirst name: {createdUser['fname']},\nLast name: {createdUser['lname']},\nUsername: {createdUser["username"]},\nPassword: {createdUser['password']}.\nThank you for trusting us.')
        else:
            ### if username exists in database, then call @static(login) method in Database and login user

            # get user password
            password = input("Please Enter your Password: ")

            # login user and get data from database
            loginedUser = Database.login(username, password)

            print(f'hello dear {loginedUser['fname']}, Welcome back, here is your information,\nFirst name: {loginedUser['fname']},\nLast name: {loginedUser['lname']},\nUsername: {loginedUser["username"]}.')