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


@patch("ai.genai")
def test_generate_summary_returns_text(mock_genai):
    """Test that generate_summary returns a string on success."""
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "This is a concise summary of the study notes."
    mock_model.generate_content.return_value = mock_response
    mock_genai.GenerativeModel.return_value = mock_model

    from ai import generate_summary
    with patch("ai.genai", mock_genai):
        mock_genai.GenerativeModel.return_value = mock_model
        result = generate_summary("Some long study notes about biology")

    assert isinstance(result, str)
    assert len(result) > 0


@patch("ai.genai")
def test_generate_summary_handles_api_error(mock_genai):
    """Test that generate_summary raises an exception on API failure."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API quota exceeded")
    mock_genai.GenerativeModel.return_value = mock_model

    from ai import generate_summary
    with patch("ai.genai", mock_genai):
        with pytest.raises(Exception) as exc_info:
            generate_summary("Test notes")
        assert "AI summary generation failed" in str(exc_info.value)


def test_summarize_route_updates_note(client):
    """Test that the summarize route generates and stores a summary."""
    fake_id = str(ObjectId())
    fake_note = {
        "_id": ObjectId(fake_id),
        "text": "Study notes about machine learning algorithms",
        "summary": None
    }

    with patch("app.notes_collection") as mock_collection, \
         patch("app.generate_summary") as mock_summary:
        mock_collection.find_one.return_value = fake_note
        mock_summary.return_value = "ML algorithms summary."
        mock_collection.update_one.return_value = MagicMock()

        response = client.post(f"/summarize/{fake_id}")
        assert response.status_code == 302
        mock_summary.assert_called_once_with(fake_note["text"])
        mock_collection.update_one.assert_called_once()
