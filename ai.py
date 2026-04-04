import os
import requests
from config import GEMINI_API_KEY

MODEL = "gemini-2.5-flash-lite"
API_ENDPOINT = f"https://aiplatform.googleapis.com/v1/publishers/google/models/{MODEL}:generateContent"


def generate_summary(text):
    """Generate a concise summary of study notes using Google Gemini."""
    try:
        url = f"{API_ENDPOINT}?key={GEMINI_API_KEY}"

        prompt = (
            "You are a study assistant. Summarize the following study notes "
            "into a clear and concise paragraph that captures the key points. "
            "Keep the summary short and useful for revision.\n\n"
            f"Study Notes:\n{text}"
        )

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()

        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise Exception(f"AI summary generation failed: {str(e)}")