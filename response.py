"""
This file contains response to be sent to the user
Author: Akshaya Revaskar
Date: 11/03/2020
"""
import json


class Response(Exception):

    def __init__(self, that):
        self.Response = that

    def jsonResponse(self, status, data):

        try:
            self.Response.send_response(status)
            self.Response.send_header('Content-type', 'text/json')
            self.Response.end_headers()
            self.Response.wfile.write(json.dumps(data, default=str).encode())
        except Exception as e:
            print(e)

    def html_response(self, status, data):

        self.Response.send_response(status)
        self.Response.send_header('Content-type', 'text/html')
        self.Response.end_headers()
        self.Response.wfile.write(data.encode("utf8"))
