"""
This file contains server specifications to run the server
Author: Akshaya Revaskar
Date: 11/03/2020
"""
from http.server import HTTPServer
from routes import Server

# declaring all the server information
def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
   server_address = (addr, port)
   httpd = server_class(server_address, handler_class)
   print('Starting httpd...')
   httpd.serve_forever()


if __name__ == "__main__":
   from sys import argv

   if len(argv) == 2:
       run(port=int(argv[1]))
   else:
       run(HTTPServer, Server)