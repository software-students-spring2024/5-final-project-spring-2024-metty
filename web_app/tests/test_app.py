from web_app.app import app, get_activity_data
from unittest.mock import patch

class Mock_User:
    def __init__(self, is_authenticated):
        self.is_authenticated = is_authenticated

class Tests:
    """Class for testing app.py"""

    def test_sanity_check(self):
        """Function sanity check."""
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_index(self):
        """Function testing index."""
        response = app.test_client().get("/")
        assert response.status_code == 200, "Expected response to return 200"

    def test_render_signup(self):
        """Function testing rendering signup page."""
        response = app.test_client().get("/signup")
        assert response.status_code == 200, "Expected response to return 200"

    def test_render_login(self):
        """Function testing rendering login page."""
        response = app.test_client().get("/login")
        assert response.status_code == 200, "Expected response to return 200"

    def test_insert_time_studied(self):
        """Function testing adding time studied to db."""
        response = app.test_client().post("/time-studied")
        assert response.status_code in (
            200,
            401,
        ), "Expected response to return 200 or 401"

    def test_get_activity_data(self):
        mock_user = Mock_User(False)
        with patch("web_app.app.current_user", mock_user):
            with app.app_context():
                response = get_activity_data()
                assert response.status_code == 200       
