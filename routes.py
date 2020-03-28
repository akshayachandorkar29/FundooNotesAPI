"""
this file has flow of execution from hitting the url to displaying the output
Author: Akshaya Revaskar
Date: 11/03/2020
"""

# importing necessary packages
from http.server import BaseHTTPRequestHandler
from views.user_view import User
from views.note_view import Note

PORT = 8000
from services.user_service import UserService
from services.note_service import NoteService
from response import Response
import requests as req
from auth.login_decorator import login_required


class Server(BaseHTTPRequestHandler):

    # this is the constructor of Server class for setting all the header values
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    # this function is used to get data from the server
    @login_required
    def do_GET(self):

        if self.path == '/logout':
            response = UserService().logout(that=self)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/read_note':
            # import pdb
            # pdb.set_trace()
            response = Note().read_note(that=self)
            if response['success']:
                user_id = response['data']
                response = NoteService().read_note(user_id)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_pin':
            response = Note().listing_pin(that=self)
            if response['success']:
                user_id = response['data']
                response = NoteService().listing_pin(user_id)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_archive':
            response = Note().listing_archive(that=self)
            if response['success']:
                user_id = response['data']
                response = NoteService().listing_archive(user_id)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_trash':
            # import pdb
            # pdb.set_trace()
            response = Note().listing_trash(that=self)
            if response['success']:
                user_id = response['data']
                response = NoteService().listing_trash(user_id)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_reminder':
            response = Note().listing_reminder(that=self)
            if response['success']:
                user_id = response['data']
                response = NoteService().listing_reminder(user_id)
            Response(self).jsonResponse(status=200, data=response)

    # this function is used to send data to the server
    @login_required
    def do_POST(self):
        # import pdb
        # pdb.set_trace()
        host = self.headers['Host']

        print(self.path.split('/?')[0])
        is_matched = self.path.split('/?')[0]
        if is_matched == '/activate':
            from urllib.parse import urlparse
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            # print(query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/activate'

        elif is_matched == '/reset':
            from urllib.parse import urlparse
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            # print(query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/reset'

        if self.path == '/register':
            response = User().register(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().register(host, user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/activate':
            response = UserService().activate(token=query_components['token'])
            return Response(self).jsonResponse(status=200, data=response)

        if self.path == '/login':
            response = User().login(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().login(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/forgot':
            response = User().forgot(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().forgot(host, user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/reset':
            response = User().reset(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().reset(token=query_components['token'], user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/create_note':
            # import pdb
            # pdb.set_trace()
            response = Note().create_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().create_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/upload_profile_pic':
            response = NoteService().upload_photo(that=self)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/collaborator':
            # import pdb
            # pdb.set_trace()
            response = Note().collaborator(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().collaborator(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)


    @login_required
    def do_PUT(self):
        # import pdb
        # pdb.set_trace()
        if self.path == '/update_note':
            response = Note().update_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().update_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/pin_note':
            response = Note().pin_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().pin_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/archive_note':
            response = Note().archive_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().archive_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/trash_note':
            response = Note().trash_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().trash_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/restore_note':
            # import pdb
            # pdb.set_trace()
            response = Note().restore_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().restore_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/set_reminder':
            response = Note().set_reminder(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().set_reminder(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

    @login_required
    def do_DELETE(self):
        if self.path == '/delete_note':
            response = Note().delete_note(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = NoteService().delete_note(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)


