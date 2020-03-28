"""
This is file for validating user data which is coming from server
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary packages
import cgi
import json
import re
from auth.validation import Validation

validation_object = Validation()


class User:

    # function for user registration
    def register(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Please Enter Proper Credentials!!!",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            result = validation_object.validating_user_data(**user_data)

            if result:
                if user_data['username'] is not None and user_data['password'] is not None and user_data['email'] is not None:
                    response["success"] = True
                    response["data"] = [user_data]

        except Exception as e:
            print(e)

        return response

    # function for user login
    def login(self, that=None):

        try:
            response = {
                "success": False,
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # reading the json data and converting it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            result = validation_object.validating_user_data(**user_data)

            if result:
                if user_data['email'] is not None and user_data['password'] is not None:
                    response["success"] = True
                    response["data"] = [user_data]

        except Exception as e:
            print(e)

        return response

    # function for logout
    # def logout(self):
    #
    #     response = {
    #         "success": True
    #     }
    #     return response

    # function for forgot password
    def forgot(self, that=None):

        try:
            response = {
                "success": False,
                "data": []
            }

            # read the message and convert it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            result = validation_object.validating_user_data(**user_data)

            if result:
                if user_data['email'] is not None:
                    response["success"] = True
                    response["data"] = [user_data]

        except Exception as e:
            print(e)

        return response

    # function for reset password
    def reset(self, that=None):

        try:
            response = {
                "success": False,
                "message": "invalid data",
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # reading the json data and converting it into a python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            result = validation_object.validating_user_data(**user_data)

            if result:
                if user_data['password'] is not None:
                    response["success"] = True
                    response["data"] = [user_data]

        except Exception as e:
            print(e)

        return response
