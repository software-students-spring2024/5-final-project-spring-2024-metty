from unittest.mock import patch
from web_app.auth import auth_signup, load_user
from web_app.app import app

class Mock_Collection:
    def __init__(self, entries):
        self.entries = entries

    def find_one(self, criteria):
        for entry in self.entries:
            if "user_id" in criteria and entry["user_id"] == criteria["user_id"]:
                return entry
        return None

    def insert_one(self, criteria):
        return True;

class Mock_Request:
    def __init__(self, form_data):
        self.form = form_data

class Tests:
    """Class for testing auth.py"""

    def test_sanity_check(self):
        """Function sanity check."""
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_load_user_found(self):
        mock_db = {"users": Mock_Collection([{"user_id": "0", "password": "1234"}])}
        with patch("web_app.auth.db", mock_db):
            user_id = "0"
            user = load_user(user_id)
            print(mock_db["users"].find_one({"user_id": user_id}))
            assert user != None and user.id == user_id

    def test_load_user_not_found(self):
        mock_db = {"users": Mock_Collection([{"user_id": "1", "password": "1234"}])}
        with patch("web_app.auth.db", mock_db):
            user_id = "0"
            user = load_user(user_id)
            print(mock_db["users"].find_one({"user_id": user_id}))
            assert user == None

    def test_auth_signup_username_taken(self):
        mock_db = {"users": Mock_Collection([{"user_id": "0", "password": "1234"}])}
        mock_form = { "username": "0", "password": "test_password", "confirm-password": "test_password"}
        mock_request = Mock_Request(mock_form)

        with app.test_request_context('/', method='POST', data=mock_form):
            with patch("web_app.auth.db", mock_db), patch("web_app.auth.request", mock_request):
                response = auth_signup()
                assert isinstance(response, str)    

    def test_auth_signup_password_mismatch(self):
        mock_db = {"users": Mock_Collection([{"user_id": "0", "password": "1234"}])}
        mock_form = { "username": "1", "password": "test_password", "confirm-password": "test_password_1"}
        mock_request = Mock_Request(mock_form)

        with app.test_request_context('/', method='POST', data=mock_form):
            with patch("web_app.auth.db", mock_db), patch("web_app.auth.request", mock_request):
                response = auth_signup()
                assert isinstance(response, str)    

    def test_insert_one(self):
        mock_db = {"users": Mock_Collection([{"user_id": "1", "password": "1234"}])}
        result = mock_db["users"].insert_one(True)
        assert result == True

