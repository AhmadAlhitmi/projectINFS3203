import pytest
from unittest.mock import patch
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test that the health check endpoint returns 200 and correct JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["app"] == "SmartNotes"


def test_home_page(client):
    """Test that the home page loads successfully."""
    with patch("app.notes_collection") as mock_collection:
        mock_collection.find.return_value.sort.return_value = []
        response = client.get("/")
        assert response.status_code == 200
        assert b"SmartNotes" in response.data