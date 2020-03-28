"""
This file has decorator for login
Author: Akshaya Revaskar
Date: 16/03/2020
"""

from response import Response
from config.redis_connection import redis_obj
import jwt

response = {
    'message': "something went wrong"
}

# creating decorator for checking user is logged in
def login_required(method):

    def token_verification(self):
        try:
            print(self.path, type(self.path))
            if self.path is ['/create_note', '/read_note']:
                # retrieving token from headers
                token = self.headers['token']

                # decoding token to get user id
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload['id']
                token = redis_obj.get(user_id)
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self)
            else:
                return method(self)
        except jwt.DecodeError:
            response['message'] = "decode error"
            Response(self).jsonResponse(status=404, data=response)
    return token_verification