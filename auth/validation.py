import re


class Validation:

    def validating_user_data(self, **user_data):
        try:
            # import pdb
            # pdb.set_trace()
            result = False

            regex_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            regex_username = r"(^[a-zA-Z][a-zA-Z0-9_-]{3,16}$)"
            regex_password = r"([A-Za-z0-9@#$%^&+=]{8,})"

            if 'email' in user_data:
                email = user_data["email"]
                if re.match(regex_email, email):
                    result = True
                else:
                    result = False
                    raise ValueError("incorrect email")

            if 'username' in user_data:
                username = user_data["username"]
                if re.match(regex_username, username):
                    result = True
                # elif regex_username.isnumeric():
                #     result = False
                #     raise ValueError("username can not be number")
                else:
                    result = False
                    raise ValueError("incorrect username")

            if 'password' in user_data:
                password = user_data["password"]
                if re.match(regex_password, password):
                    result = True
                else:
                    result = False
                    raise ValueError("incorrect password... length must be 8 or more!!!")

        except ValueError as err:
            print(err)
        except Exception as e:
            print(e)

        return result