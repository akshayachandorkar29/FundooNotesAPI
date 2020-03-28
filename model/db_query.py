"""
this is the file containing database queries for different operations
Author: Akshaya Revaskar
Date: 11/03/2020
"""

from config.db_connection import Connection


class Query:
    """This class is used to form connection with the database and perform operation check
       entry into the database
    """

    def __init__(self):  # This function is used to form a connection with database
        self.mydb = Connection()

    # function for insert
    def insert(self, user_data, table_name):

        # declaring empty lists
        list_keys = []
        list_val = []

        # getting keys and values from dictionary and storing them into respective lists
        for key, val in user_data.items():
            list_keys.append(key)
            list_val.append(val)

        query_placeholders = ', '.join(['%s'] * len(list_val))
        query_columns = ', '.join(list_keys)

        query = f" insert into {table_name} (%s) values (%s) " % (query_columns, query_placeholders)

        self.mydb.query_execute(query=query, value=list_val)

    # function for read
    def read(self, table_name, column_name, column_value):
        # import pdb
        # pdb.set_trace()

        if column_name is None and column_value is None:
            query = f"select * from {table_name}"
            result = self.mydb.run_query(query=query)
        else:
            query = f"select * from {table_name} where {column_name} = {column_value}"
            # query = f"select * from {table_name} where %s = %s" % (column_name, column_value)
            result = self.mydb.run_query(query=query)

        return result

    # function for update
    def update(self, user_data, table_name):
        # import pdb
        # pdb.set_trace()
        column = []
        rows_values = []
        val = []
        id = 0
        for key, values in user_data.items():
            if key != 'id':
                column.append(key)
                val.append(values)
            if key == 'id':
                id = values

        val.append(id)
        set_tokens = ','.join([f'{x}=%s' for x in column])
        query = f"update {table_name} set {set_tokens} where id = %s"
        self.mydb.query_execute(query=query, value=val)

    # function for delete
    def delete(self, table_name, column_name, column_value):

        query = f"delete from {table_name} where {column_name} = {column_value}"
        self.mydb.query_execute(query)
