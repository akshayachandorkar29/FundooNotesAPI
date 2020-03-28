"""
This file contains business logic for connecting mysql server with localhost
Author: Akshaya Revaskar
Date: 11/03/2020
"""
# importing required packages
import os
from dotenv import load_dotenv
import mysql.connector
from config.singleton import singleton
load_dotenv()

@singleton
class Connection:

    # this is the constructor of the class Connection
    def __init__(self, **kwargs):
        self.conn = self.connect(**kwargs)
        self.mycursor = self.conn.cursor()

    def connect(self, **kwargs):
        mydb = mysql.connector.connect(
            host=kwargs["host"],
            user=kwargs["user"],
            passwd=kwargs["passwd"],
            database=kwargs["database"],
        )
        return mydb

    def run_query(self, query, value=None):
        self.mycursor.execute(query, value)
        return self.mycursor.fetchall()

    def query_execute(self, query, value=None):
        self.mycursor.execute(query, value)
        self.conn.commit()


con = Connection(host=os.getenv("HOST"),
                 user=os.getenv("USER"),
                 passwd=os.getenv("PASSWD"),
                 database=os.getenv("DATABASE"))

