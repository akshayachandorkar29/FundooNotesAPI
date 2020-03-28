"""
This file contains test cases
Author: Akshaya Revaskar
Date: 11/03/2020
"""
import requests
import jwt
import re
import json
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
import pytest


class TestRegistration:

    def test_registration_username_not_given(self):
        url = os.getenv("base_url") + '/register'
        data = {'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_password_not_given(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_email_not_given(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_username_starting_with_letter(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': '3425sunita', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_username_is_number(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': '342545', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_username_is_less_than_4(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sun', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_username_is_greater_than_16(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunitabalkrishnamudaliar', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_password_is_less_than_8(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_email_missing_at_the_rate(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29', 'email': 'mudaliarsunita29gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_email_missing_dot(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmailcom'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_blank_username(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': '', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_blank_password(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': '', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_blank_email(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29', 'email': ''}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_same_email(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29', 'email': 'akshayachandorkar29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_registration_successful(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'sunita', 'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

class TestLogin:

    def test_login_email_not_given(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_password_not_given(self):
        url = os.getenv("base_url") + '/login'
        data = {'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_email_not_having_at_the_rate(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29', 'email': 'mudaliarsunita29.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_email_not_having_dot(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29', 'email': 'mudaliarsunita29@gmailcom'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_wrong_email(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29', 'email': 'akshayachandorkar29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_password_less_than_8(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_wrong_password(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'suniat', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_blank_email(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita', 'email': ''}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_blank_password(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': '', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_not_activated(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': '', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login_successful(self):
        import mysql.connector

        mydb = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            passwd=os.getenv("PASSWD"),
            database=os.getenv("DATABASE")
        )
        mycursor = mydb.cursor()
        sql = f"update user set active = 1 where email = 'akshayachandorkar29@gmail.com' "
        mycursor.execute(sql)
        mydb.commit()
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestForgot:

    def test_forgot_email_not_given(self):
        url = os.getenv("base_url") + '/forgot'
        data = {}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_forgot_wrong_email_given(self):
        url = os.getenv("base_url") + '/forgot'
        data = {'email': 'sunita.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_forgot_successful(self):
        url = os.getenv("base_url") + '/forgot'
        data = {'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

class TestLogout:

    def test_logout_not_logged_In(self):
        url = os.getenv("base_url") + '/logout'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_logout_successful(self):
        url = os.getenv("base_url") + '/logout'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_login(self):
        url = os.getenv("base_url") + '/login'
        data = {'password': 'sunita@29', 'email': 'mudaliarsunita29@gmail.com'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestCreateNote:

    def test_create_note_title_not_given(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'description': 'making new notes', 'color': 'red'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_description_not_given(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': 'eighth note', 'color': 'red'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_color_not_given(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': 'eighth note', 'description': 'making new notes'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_empty_title(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': '', 'description': 'making new notes', 'color': 'red'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_empty_description(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': 'tength note', 'description': '', 'color': 'red'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_empty_color(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': 'eighth note', 'description': 'making new notes', 'color': ''}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_not_logged_in(self):
        url = os.getenv("base_url") + '/create_note'
        data = {'title': 'fifteenth note', 'description': 'making new notes', 'color': 'wine'}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_create_note_successful(self):
        url = os.getenv("base_url") + '/create_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'title': 'new note', 'description': 'making new notes', 'color': 'wine'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestReadNote:

    def test_read_note_not_logged_in(self):
        url = os.getenv("base_url") + '/read_note'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_read_note_successful(self):
        url = os.getenv("base_url") + '/read_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

class TestUpdateNote:

    def test_update_note_not_logged_in(self):
        url = os.getenv("base_url") + '/update_note'
        data = {'id': 37, 'description': 'updating the new notes'}
        headers = {'content_type': "application/json"}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_update_note_successful(self):
        url = os.getenv("base_url") + '/update_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'description': 'updating the new notes'}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestPinNote:

    def test_pin_note_not_logged_in(self):
        url = os.getenv("base_url") + '/pin_note'
        data = {'id': 37, 'is_pinned': 1}
        headers = {'content_type': "application/json"}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_pin_note_successful(self):
        url = os.getenv("base_url") + '/pin_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'is_pinned': 1}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestArchiveNote:

    def test_archive_note_not_logged_in(self):
        url = os.getenv("base_url") + '/archive_note'
        data = {'id': 37, 'is_archived': 1}
        headers = {'content_type': "application/json"}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_archive_note_successful(self):
        url = os.getenv("base_url") + '/archive_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'is_archived': 1}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestTrashNote:

    def test_trash_note_not_logged_in(self):
        url = os.getenv("base_url") + '/trash_note'
        data = {'id': 37, 'is_trashed': 1}
        headers = {'content_type': "application/json"}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_trash_note_successful(self):
        url = os.getenv("base_url") + '/trash_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'is_trashed': 1}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestRestoreNote:

    def test_restore_note_not_logged_in(self):
        url = os.getenv("base_url") + '/restore_note'
        data = {'id': 37, 'is_restored': 1}
        headers = {'content_type': "application/json"}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_restore_note_successful(self):
        url = os.getenv("base_url") + '/restore_note'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'is_restored': 1}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestListingPinnedNotes:

    def test_listing_pin_note_not_logged_in(self):
        url = os.getenv("base_url") + '/listing_pin'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_listing_pin_notes_successful(self):
        url = os.getenv("base_url") + '/listing_pin'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestListingArchivedNotes:

    def test_listing_archive_note_not_logged_in(self):
        url = os.getenv("base_url") + '/listing_archive'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_all_archive_notes_successful(self):
        url = os.getenv("base_url") + '/listing_archive'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestListingTrashedNotes:

    def test_listing_trash_note_not_logged_in(self):
        url = os.getenv("base_url") + '/listing_trash'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_all_trash_notes_successful(self):
        url = os.getenv("base_url") + '/listing_trash'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestReminderNote:
    def test_reminder_note_empty_reminder(self):
        url = os.getenv("base_url") + '/set_reminder'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'reminder': ""}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_reminder_note_reminder_not_given(self):
        url = os.getenv("base_url") + '/set_reminder'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_reminder_note_successful(self):
        url = os.getenv("base_url") + '/set_reminder'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'id': 37, 'reminder': "2020-03-28 10:45:00"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.put(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestListingReminderNotes:

    def test_listing_reminder_note_not_logged_in(self):
        url = os.getenv("base_url") + '/listing_reminder'
        headers = {'content_type': "application/json"}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_all_reminder_notes_successful(self):
        url = os.getenv("base_url") + '/listing_reminder'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        headers = {'content_type': "application/json", 'token': token}
        res = requests.get(url=url, headers=headers)
        print(res.text)
        assert res.status_code == 200


class TestCollaborator:

    def test_collaborate_note_not_logged_in(self):
        url = os.getenv("base_url") + '/collaborator'
        data = {'note_id': 37, 'email': "akshayachandorkar29gmail.com"}
        headers = {'content_type': "application/json"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_collaborator_not_having_at_the_rate_in_email(self):
        url = os.getenv("base_url") + '/collaborator'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'note_id': 37, 'email': "akshayachandorkar29gmail.com"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_collaborator_not_having_dot_in_email(self):
        url = os.getenv("base_url") + '/collaborator'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'note_id': 37, 'email': "akshayachandorkar29@gmailcom"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_collaborator_user_does_not_exists(self):
        url = os.getenv("base_url") + '/collaborator'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'note_id': 37, 'email': "prathmeshtalkar@gmail.com"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_collaborator_given_note_not_belongs_to_user(self):
        url = os.getenv("base_url") + '/collaborator'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'note_id': 14, 'email': "akshayachandorkar29@gmailcom"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

    def test_collaborate_note_successful(self):
        url = os.getenv("base_url") + '/collaborator'
        text = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjZ9.9zD7rBTIfj9tGtKpk0y1gA8XHQnjf-puqsBidDMe5zs"
        token = re.sub(r"\s+", " ", text, flags=re.I)
        data = {'note_id': 37, 'email': "akshayachandorkar29@gmailcom"}
        headers = {'content_type': "application/json", 'token': token}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200
