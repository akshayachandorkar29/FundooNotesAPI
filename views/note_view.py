"""
This is file for validating notes data coming from server
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary packages
import json
import jwt
import re
from auth.validation import Validation
validation_object = Validation()


class Note:

    # CREATE NOTE API
    def create_note(self, that=None):

        try:
            response = {
                "success": False,
                "message": "enter valid data",
                "data": []
            }
            # import pdb
            # pdb.set_trace()
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # decoding token to get the id
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')

                # adding user_id in json_data dictionary
                user_data["user_id"] = user_id

                # validating user entered data
                if user_data["title"] is None:
                    response["success"] = False
                    response['message'] = 'title can not be empty'

                if user_data["description"] is None:
                    response["success"] = False
                    response['message'] = 'description can not be empty'

                if user_data["color"] is None:
                    response["success"] = False
                    response['message'] = 'color can not be empty'

                if len(user_data["title"]) > 0 and len(user_data["description"]) > 0 and len(user_data["color"]) > 0:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]

            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except Exception as e:
            print(e)

        return response

    # READ NOTE API
    def read_note(self, that=None):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # getting token from headers
            token = that.headers['token']

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "something went wrong"
            else:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                response["success"] = True
                response["message"] = "you got the token"
                response["data"] = user_id

        except Exception as e:
            print(e)

        return response

    # UPDATE NOTE API
    def update_note(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()
            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:

                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "give note id to update the note"
                else:
                # if len(user_data["id"]) > 0:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except Exception as e:
            print(e)

        return response

    # DELETE NOTE API
    def delete_note(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:

                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "give note id to delete the note"
                else:
                    # if len(user_data["id"]) > 0:
                    response["success"] = True
                    response['message'] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except Exception as e:
            print(e)

        return response

    # PIN NOTE API
    def pin_note(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating json data
                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                if user_data["is_pinned"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False

        except Exception as e:
            print(e)

        return response

    # ARCHIVE NOTE API
    def archive_note(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                if user_data["is_archived"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False

        except Exception as e:
            print(e)

        return response

    # TRASH NOTE API
    def trash_note(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                if user_data["is_trashed"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
        except Exception as e:
            print(e)

        return response

    # RESTORE NOTE API
    def restore_note(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating data coming from user
                if user_data["id"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                if user_data["is_restored"] is None:
                    response["success"] = False
                    response["message"] = "something went wrong"
                else:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False

        except Exception as e:
            print(e)

        return response

    # LISTING PIN NOTE API
    def listing_pin(self, that=None):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # getting token from headers
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "something went wrong"
            else:
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id
        except Exception as e:
            print(e)

        return response

    # LISTING ARCHIVE NOTE API
    def listing_archive(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            # import pdb
            # pdb.set_trace()

            # getting token from headers
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "something went wrong"
            else:
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            print(e)

        return response

    # LISTING TRASH NOTE API
    def listing_trash(self, that=None):
        try:
            response = {

                "success": False,
                "message": "something went wrong"
            }

            # getting token from headers
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "something went wrong"
            else:
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            print(e)

        return response

    # REMINDER API
    def set_reminder(self, that=None):

        try:
            response = {

                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # reading the json data and converting it into python dictionary
            length = int(that.headers['Content-Length'])
            message = that.rfile.read(length)
            user_data = json.loads(message)

            # retriving token from headres to retrive id of the user who is logged in
            token = that.headers['token']
            if token:
                # validating user entered data
                if user_data["reminder"] is None:
                    response['message'] = 'set date to remind'

                if user_data["id"] is None:
                    response['message'] = 'give note id to set reminder'

                if len(user_data["reminder"]) > 0:
                    response["success"] = True
                    response["message"] = "valid data"
                    response["data"] = [user_data]
            else:
                response["success"] = False
                response["message"] = "You have to LOGIN first"

        except Exception as e:
            print(e)

        return response

    # LISTING REMINDER NOTE API
    def listing_reminder(self, that=None):
        try:
            response = {

                "success": False,
                "message": "something went wrong"
            }
            # getting token from headers
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')

            # validating token
            if token is None:
                response["success"] = False
                response["message"] = "something went wrong"
            else:
                response["success"] = True
                response["message"] = "valid data"
                response["data"] = user_id

        except Exception as e:
            print(e)

        return response

    # API for collaborating note
    def collaborator(self, that=None):
        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # getting token from headers
            token = that.headers['token']

            if token:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')

                # reading the json data and converting it into python dictionary
                length = int(that.headers['Content-Length'])
                message = that.rfile.read(length)
                user_data = json.loads(message)

                # adding user id into user data dictionary
                user_data['user_id'] = user_id

                # validating user data
                result = validation_object.validating_user_data(**user_data)

                if result:
                    if user_data is not None:
                        response["success"] = True
                        response["data"] = [user_data]
            else:
                response["success"] = False
        except Exception as e:
            print(e)

        return response

