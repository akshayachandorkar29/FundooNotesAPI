"""
This file contains note services
Author: Akshaya Revaskar
Date: 13/03/2020
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
# redis_obj = RedisConnection()


class NoteService:

    def __init__(self):
        self.mydb = Connection()
        self.redis_obj = RedisConnection()

    # CREATE NOTE API
    def create_note(self, user_data):
        try:
            response = {
                "success": False,
                "message": "Something went wrong!"
            }
            # import pdb
            # pdb.set_trace()
            table_name = "notes"

            # firing sql query to insert the note
            database_obj.insert(user_data, table_name)

            response["success"] = True
            response["message"] = "NOTE CREATED SUCCESSFULLY!"

        except Exception as e:
            print(e)

        return response

    # READ NOTE API
    def read_note(self, user_id):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            table_name = "notes"
            column_name = "user_id"
            column_value = user_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            if read:
                # adding notes in the list which are not trashed and archived
                all_notes = []
                res = []
                for record in read:
                    # unpacking tuple
                    db_id, db_user_id, db_title, db_description, db_color, db_is_pinned, db_is_archived, db_created_at, \
                    db_modified_at, db_is_trashed, db_is_restored, db_reminder = record

                    # checking if note is trashed or note is archived
                    if db_is_archived == 0 and db_is_trashed == 0:
                        all_notes.append(record)

                for record in all_notes:
                    new_list = list(record)

                    all_keys = ["id", "user_id", "title", "description", "color", "is_pinned", "is_archived",
                                "created_at", "modified_at", "is_trashed", "is_restored"]

                    dictionary = {all_keys[i]: new_list[i] for i in range(len(all_keys))}

                    res.append(dictionary)

                    response["success"] = True
                    response["message"] = "NOTE READ SUCCESSFULLY!"
                    response["data"] = res

            else:
                response["success"] = False
                response["message"] = "something went wrong!"

        except Exception as e:
            print(e)

        return response

    # UPDATE NOTE API
    def update_note(self, user_data):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            table_name = "notes"

            # firing query to update note
            database_obj.update(user_data, table_name)

            response["success"] = True
            response["message"] = "NOTE UPDATED SUCCESSFULLY"

        except Exception as e:
            print(e)

        return response

    # DELETE NOTE API
    def delete_note(self, user_data):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            user_id = user_data["id"]
            table_name = "notes"
            column_name = "id"
            column_value = user_id

            # reading data of the given note id
            read = database_obj.read(table_name, column_name, column_value)
            is_trashed = read[0][9]

            # checking read note is trashed or not
            if is_trashed == 1:
                # if trash true, firing query to delete the note
                database_obj.delete(table_name, column_name, column_value)
                response["success"] = True
                response["message"] = "NOTE DELETED SUCCESSFULLY"
            else:
                # firing query to send the note in trash
                user_data["is_trashed"] = 1
                database_obj.update(user_data, table_name)

                response["success"] = True
                response["message"] = "NOTE TRASHED SUCCESSFULLY"

        except Exception as e:
            print(e)

        return response

    # PIN NOTE API
    def pin_note(self, user_data):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            table_name = "notes"

            # firing query to pin the note
            database_obj.update(user_data, table_name)

            response["success"] = True
            response["message"] = "NOTE PINNED SUCCESSFULLY"

        except Exception as e:
            print(e)

        return response

    # ARCHIVE NOTE API
    def archive_note(self, user_data):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            table_name = "notes"

            # firing query to archive note
            database_obj.update(user_data, table_name)

            response["success"] = True
            response["message"] = "NOTE ARCHIVED SUCCESSFULLY"

        except Exception as e:
            print(e)

        return response

    # TRASH NOTE API
    def trash_note(self, user_data):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            note_id = user_data["id"]
            table_name = "notes"

            user_data["is_restored"] = 0
            # firing query to trash note
            database_obj.update(user_data, table_name)

            response["success"] = True
            response["message"] = "NOTE TRASHED SUCCESSFULLY"

        except Exception as e:
            print(e)

        return response

    # RESTORE NOTE API
    def restore_note(self, user_data):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()
            note_id = user_data["id"]
            table_name = "notes"
            column_name = "id"
            column_value = note_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            is_trashed = read[0][9]

            # update_trash = {"id": note_id}
            if read:
                # checking if note is trashed
                if is_trashed == 1:
                    user_data["is_trashed"] = 0

                    # firing query to restore note
                    database_obj.update(user_data, table_name)
                    response["success"] = True
                    response["message"] = "NOTE RESTORED SUCCESSFULLY!"
            else:
                response["success"] = False
                response["message"] = "something went wrong!"

        except Exception as e:
            print(e)

        return response

    # LISTING PIN NOTE API
    def listing_pin(self, user_id):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            table_name = "notes"
            column_name = "user_id"
            column_value = user_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            if read:
                all_notes = []
                data = []
                # traversing result of read
                for record in read:
                    # unpacking tuple
                    db_id, db_user_id, db_title, db_description, db_color, db_is_pinned, db_is_archived, db_created_at, \
                    db_modified_at, db_is_trashed, db_is_restored, db_reminder = record
                    # checking if note is pinned
                    if db_is_pinned == 1:
                        # append the record
                        all_notes.append(record)

                # traversing the all notes list
                for record in all_notes:
                    new_list = list(record)

                    # adding keys of database in list
                    all_keys = ["id", "user_id", "title", "description", "color", "is_pinned", "is_archived",
                                "created_at", "modified_at", "is_trashed", "is_restored", "reminder"]

                    # merging key and values to form a dictionary to return
                    dictionary = {all_keys[i]: new_list[i] for i in range(len(all_keys))}

                    data.append(dictionary)

                    response["success"] = True
                    response["message"] = "ALL PINNED NOTES READ SUCCESSFULLY!"
                    response["data"] = data

            if len(all_notes) == 0:
                response["success"] = False
                response["message"] = "NO PINNED NOTES FOUND!"

        except Exception as e:
            print(e)

        return response

    # LISTING ARCHIVE NOTE API
    def listing_archive(self, user_id):
        try:
            response = {

                "success": False,
                "message": "something went wrong"
            }

            table_name = "notes"
            column_name = "user_id"
            column_value = user_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            if read:
                # adding notes in the list which are not trashed and archived
                all_notes = []
                data = []
                # traversing read list
                for record in read:
                    # unpacking tuple
                    db_id, db_user_id, db_title, db_description, db_color, db_is_pinned, db_is_archived, db_created_at, \
                    db_modified_at, db_is_trashed, db_is_restored, db_reminder = record
                    # checking if note archived
                    if db_is_archived == 1:
                        all_notes.append(record)

                # traersing new list
                for record in all_notes:
                    new_list = list(record)

                    # adding keys into list
                    all_keys = ["id", "user_id", "title", "description", "color", "is_pinned", "is_archived",
                                "created_at", "modified_at", "is_trashed", "is_restored", "reminder"]

                    # merging key and values to form a dictionary to return
                    dictionary = {all_keys[i]: new_list[i] for i in range(len(all_keys))}

                    data.append(dictionary)

                    response["success"] = True
                    response["message"] = "ALL ARCHIVED NOTES READ SUCCESSFULLY!"
                    response["data"] = data

            if len(all_notes) == 0:
                response["success"] = False
                response["message"] = "NO ARCHIVED NOTES FOUND!"

        except Exception as e:
            print(e)

        return response

    # LISTING TRASH NOTE API
    def listing_trash(self, user_id):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            table_name = "notes"
            column_name = "user_id"
            column_value = user_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            if read:
                # adding notes in the list which are not trashed and archived
                all_notes = []
                data = []
                for record in read:
                    # unpacking tuple
                    db_id, db_user_id, db_title, db_description, db_color, db_is_pinned, db_is_archived, db_created_at, \
                    db_modified_at, db_is_trashed, db_is_restored, db_reminder = record

                    # checking if note is trashed
                    if db_is_trashed == 1:
                        all_notes.append(record)

                for record in all_notes:
                    new_list = list(record)

                    # adding keys into list
                    all_keys = ["id", "user_id", "title", "description", "color", "is_pinned", "is_archived",
                                "created_at", "modified_at", "is_trashed", "is_restored", "reminder"]

                    # merging key and values to form a dictionary to return
                    dictionary = {all_keys[i]: new_list[i] for i in range(len(all_keys))}

                    data.append(dictionary)

                    response["success"] = True
                    response["message"] = "ALL TRASHED NOTES READ SUCCESSFULLY!"
                    response["data"] = data

            if len(all_notes) == 0:
                response["success"] = False
                response["message"] = "NO TRASHED NOTES FOUND!"

        except Exception as e:
            print(e)

        return response

    # API FOR UPLOADING PROFILE PIC
    def upload_photo(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            import cgi
            import os

            # parsing the headers and storing in the dictionary
            ctype, pdict = cgi.parse_header(that.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

            if ctype == 'multipart/form-data':
                form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                                                                      'CONTENT_TYPE': that.headers[
                                                                                          'Content-Type'], })

                # storing form data into a file
                filename = form['upfile'].filename

                # reading the contents of file and saving it into data
                data = form['upfile'].file.read()

                # adding the photo into media directory
                open("./media/%s" % filename, "wb").write(data)
                path = f"./media/{filename}"

                # getting token from header
                token = that.headers['token']

                # decoding token to get the id
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                user_data = {"user_id": user_id, "path": path}
                database_obj.insert(user_data=user_data, table_name="profile")

                response["success"] = True
                response["message"] = "PHOTO UPLOADED SUCCESSFULLY!"

            else:
                response["success"] = False
                response["message"] = "Something went wrong! Unsuccessful..."

        except Exception as e:
            print(e)

        return response

    # REMINDER API
    def set_reminder(self, user_data):
        try:
            response = {
                "success": False,
                "message": "Something went wrong!",
                "data": []
            }

            table_name = "notes"

            # firing sql query to update the note
            database_obj.update(user_data, table_name)

            response["success"] = True
            response["message"] = "REMINDER SET SUCCESSFULLY!"

        except Exception as e:
            print(e)

        return response

    # LISTING REMINDER NOTE API
    def listing_reminder(self, user_id):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            table_name = "notes"
            column_name = "user_id"
            column_value = user_id

            # firing query to read the note
            read = database_obj.read(table_name, column_name, column_value)

            if read:
                # adding notes in the list which are not trashed and archived
                all_notes = []
                data = []
                for record in read:
                    # unpacking tuple
                    db_id, db_user_id, db_title, db_description, db_color, db_is_pinned, db_is_archived, db_created_at, \
                    db_modified_at, db_is_trashed, db_is_restored, db_reminder = record

                    if db_reminder == None:
                        pass
                    else:
                        all_notes.append(record)

                for record in all_notes:
                    new_list = list(record)

                    all_keys = ["id", "user_id", "title", "description", "color", "is_pinned", "is_archived",
                                "created_at", "modified_at", "is_trashed", "is_restored", "reminder"]

                    dictionary = {all_keys[i]: new_list[i] for i in range(len(all_keys))}

                    data.append(dictionary)

                    response["success"] = True
                    response["message"] = "ALL NOTES WITH REMINDER READ SUCCESSFULLY!"
                    response["data"] = data
            else:
                response["success"] = False
                response["message"] = "NO NOTES WITH REMINDER FOUND!"

        except Exception as e:
            print(e)

        return response

    # API FOR COLLABORATING NOTE
    def collaborator(self, user_data):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace()

            # extracting user email id from json dictionary
            user_email = user_data["email"]

            # reading all the user data
            read_user_data = database_obj.read(table_name="user", column_name=None, column_value=None)
            user_email_list = []
            for tupleRecord in read_user_data:
                db_email = tupleRecord[3]
                user_email_list.append(db_email)

            emailExist = False
            # traversing the note id list to check whether given note belongs to user logged in
            for i in user_email_list:
                if user_email == i:
                    emailExist = True

            if emailExist:

                # reading all the notes of the user who is logged in
                read = database_obj.read(table_name="notes", column_name="user_id", column_value=user_data["user_id"])

                # creating list to keep all the note's id belongs to logged in person
                note_id_list = []

                # traversing the read list to store note id
                for record in read:
                    db_note_id = record[0]
                    note_id_list.append(db_note_id)

                isPresent = False
                # traversing the note id list to check whether given note belongs to user logged in
                for i in note_id_list:
                    if user_data['note_id'] == i:
                        isPresent = True

                table_name = "collaborator"
                if isPresent:
                    database_obj.insert(user_data, table_name)
                    note_details = database_obj.read(table_name="notes", column_name="id", column_value=user_data['note_id'])

                    # message to send in the mail as a link
                    message = f"Hello!!! I have shared the note with you.......\n\n" \
                              f"Details of note : {note_details}"

                    # sending mail using token, email id and link
                    mail_object.send_mail(None, user_email, message)

                    response["success"] = True
                    response["message"] = "NOTE COLLABORATED!"
            else:
                response["success"] = False
                response["message"] = "USER DOES NOT EXIST!!!"

        except Exception as e:
            print(e)
        return response

