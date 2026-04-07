import pytest
from unittest.mock import patch, MagicMock
from bson.objectid import ObjectId
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page_returns_200(client):
    """Test that the home page loads successfully."""
    with patch("app.notes_collection") as mock_collection:
        mock_collection.find.return_value.sort.return_value = []
        response = client.get("/")
        assert response.status_code == 200
        assert b"SmartNotes" in response.data


def test_health_endpoint_returns_json(client):
    """Test that the health endpoint returns correct JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["app"] == "SmartNotes"


def test_add_note_with_valid_input(client):
    """Test that a valid note is saved and redirects to home."""
    with patch("app.notes_collection") as mock_collection:
        mock_collection.insert_one.return_value = MagicMock(inserted_id="123")
        response = client.post("/notes", data={"text": "Test study note"})
        assert response.status_code == 302
        mock_collection.insert_one.assert_called_once()


def test_add_note_redirects_to_home(client):
    """Test that adding a note redirects back to the home page."""
    with patch("app.notes_collection") as mock_collection:
        mock_collection.insert_one.return_value = MagicMock()
        response = client.post(
            "/notes",
            data={"text": "Another note"},
            follow_redirects=False
        )
        assert response.status_code == 302
        assert "/" in response.headers["Location"]


def test_delete_note_with_valid_id(client):
    """Test that a note can be deleted with a valid ObjectId."""
    fake_id = str(ObjectId())
    with patch("app.notes_collection") as mock_collection:
        mock_collection.delete_one.return_value = MagicMock(deleted_count=1)
        response = client.post(f"/delete/{fake_id}")
        assert response.status_code == 302
        mock_collection.delete_one.assert_called_once()
