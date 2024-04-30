from unittest.mock import patch
from web_app.auth import load_user


class Mock_Collection:
    def __init__(self, entries):
        self.entries = entries

    def find_one(self, criteria):
        for entry in self.entries:
            if "user_id" in criteria and entry["user_id"] == criteria["user_id"]:
                return entry
        return None


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
