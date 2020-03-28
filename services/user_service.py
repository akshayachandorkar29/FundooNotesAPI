"""
This file contains user services
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary modules
import jwt
from config.db_connection import Connection
from config.redis_connection import RedisConnection
from model.db_query import Query
from vendor.send_mail import SendMail
from auth.short_url_generator import ShortUrlGenerator

short_object = ShortUrlGenerator()
mail_object = SendMail()
database_obj = Query()
# redis_obj = RedisConnection


class UserService:

    def __init__(self):
        self.mydb = Connection()
        self.redis_obj = RedisConnection()

    # function for user registration take argument user_data which is data given by user
    def register(self, host, user_data):
        try:
            # import pdb
            # pdb.set_trace()
            # initial response message
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }

            # retriving all the data from table
            table_name = "user"
            read = database_obj.read(table_name, None, None)

            # checking email already exist
            for record in read:
                db_id, db_username, db_password, db_email, db_active = record
                if db_username == user_data["username"] or db_email == user_data["email"]:
                    response['success'] = True
                    response['message'] = 'Already Registered!!!'
                    break

            if response['success'] == False:

                table_name = "user"
                # inserting data into table
                database_obj.insert(user_data, table_name)

                column_name = 'username'
                column_value = user_data['username']

                # retriving record given email id
                db_record = database_obj.read(table_name, column_name, f"'{column_value}'")
                print(db_record)
                db_record = db_record[0]
                db_id, db_username, db_password, db_email, db_active = db_record

                # generating token using JWT module
                token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')

                short = short_object.short_url(10)

                secure_data = {"token": token, "short": short}

                table_name = "secure"

                # inserting data into secure table
                database_obj.insert(secure_data, table_name)

                # message to send in the mail as a link
                message = f"Click here to activate : http://{host}/activate/?token={short}"

                # sending mail using token, email id and link
                mail_object.send_mail(token, db_email, message)

                response["success"] = True,
                response["message"] = "User Registered successfully!"

        except Exception as e:
            print(e)

        return response

    def activate(self, token):
        try:

            # initial response message
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }

            # retriving all the data from table
            table_name = "secure"
            read = database_obj.read(table_name, None, None)

            column_name = "short"
            l_token = []
            # token = str(token)
            for record in read:
                db_id, db_short, db_token = record
                if db_short == token:
                    column_value = f"'{token}'"
                    l_token = database_obj.read(table_name, column_name, column_value)
                    break

            l_token = l_token[0][2]
            payload = jwt.decode(l_token, 'secret', algorithms=['HS256'])

            user_id = payload.get('id')
            user_data = {"id": user_id, "active": "1"}
            database_obj.update(user_data, table_name="user")
            response["success"] = True
            response["message"] = "You Are Activated!"

        except Exception as e:
            print(e)

        return response

    # function to login inside the system using saved credentials
    def login(self, user_data):
        try:
            response = {
                "success": False,
                "message": "Unable to login",
                "data": []
            }
            # import pdb
            # pdb.set_trace()
            table_name = "user"
            # retrieving all the data from database
            db_data = database_obj.read(table_name, None, None)

            # unpacking dictionary values
            user_email = user_data["email"]
            user_pass = user_data["password"]

            # matching user entered and database credentials
            for record in db_data:
                db_id, db_username, db_password, db_email, db_active = record
                if db_email == user_email and db_password == user_pass and db_active == '1':

                    # generating token using JWT module
                    token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')

                    # setting data into redis cache
                    self.redis_obj.set(db_id, token)

                    response["success"] = True
                    response["message"] = "Successfully logged in!"
                    response["data"] = [{"token": token}]
                    break
        except Exception as e:
            print(e)

        return response

    # function to log out the user from the system
    def logout(self, that=None):
        try:

            response = {
                "success": False,
                "message": "Unable to logout",
                "data": []
            }

            # getting token from headers
            token = that.headers['token']

            # decoding token to get the user id
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

            user_id = payload.get('id')

            # deleting user of the same id from redis cache
            self.redis_obj.delete(user_id)

            response["success"] = True
            response["message"] = "Successfully logged out!"

        except Exception as e:
            print(e)

        return response

    # function will send mail to user in case user forgets password
    def forgot(self, host, user_data):
        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }

            table_name = "user"

            # reading data from database to match the email id
            db_data = database_obj.read(table_name, None, None)

            user_email = user_data["email"]

            # checking record to match user entered and database email id
            for record in db_data:
                db_id, db_username, db_password, db_email, db_active = record
                if db_email == user_email:

                    # generating token with JWT module
                    token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')

                    short = short_object.short_url(10)

                    table_name = "secure"
                    secure_data = {"token": token, "short": short}

                    database_obj.insert(secure_data, table_name)

                    # message to send with email
                    message = f"Click here to reset the password : http://{host}/reset/?token=" + short

                    # sending mail using token and message if email id get matched
                    mail_object.send_mail(token, user_email, message)

                    response["success"] = True
                    response["message"] = "Mail sent successfully!"

        except Exception as e:
            print(e)

        return response

    # function for resetting password in case of user forget it
    # it will take user_data: new password to set
    def reset(self, user_data, token):
        try:

            response = {
                "success": True,
                "message": "Password Reset successfully!",
                "data": []
            }
            # import pdb
            # pdb.set_trace()
            table_name = "secure"
            read = database_obj.read(table_name, None, None)

            column_name = "short"
            l_token = []
            # token = str(token)
            for record in read:
                db_id, db_short, db_token = record
                if db_short == token:
                    column_value = f"'{token}'"
                    l_token = database_obj.read(table_name, column_name, column_value)
                    break

            l_token = l_token[0][2]

            payload = jwt.decode(l_token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            user_data["id"] = user_id
            table_name = "user"

            # inserting data into the table
            database_obj.update(user_data, table_name)

        except Exception as e:
            print(e)

        return response