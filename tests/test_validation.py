import pytest
from unittest.mock import patch
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_empty_input_rejected(client):
    """Test that an empty note is rejected with a flash message."""
    with patch("app.notes_collection") as mock_collection:
        response = client.post(
            "/notes",
            data={"text": ""},
            follow_redirects=True
        )
        assert response.status_code == 200
        assert b"Note cannot be empty" in response.data
        mock_collection.insert_one.assert_not_called()


def test_whitespace_only_input_rejected(client):
    """Test that whitespace-only input is rejected."""
    with patch("app.notes_collection") as mock_collection:
        response = client.post(
            "/notes",
            data={"text": "   "},
            follow_redirects=True
        )
        assert response.status_code == 200
        assert b"Note cannot be empty" in response.data
        mock_collection.insert_one.assert_not_called()


def test_valid_note_text_accepted(client):
    """Test that valid text input is accepted and saved."""
    with patch("app.notes_collection") as mock_collection:
        response = client.post(
            "/notes",
            data={"text": "Valid study notes about Python"},
            follow_redirects=True
        )
        assert response.status_code == 200
        mock_collection.insert_one.assert_called_once()
        saved_note = mock_collection.insert_one.call_args[0][0]
        assert saved_note["text"] == "Valid study notes about Python"
        assert saved_note["summary"] is None
