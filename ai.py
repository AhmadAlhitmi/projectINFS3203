import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_summary(text):
    """Generate a concise summary of study notes using Google Gemini."""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = (
            "You are a study assistant. Summarize the following study notes "
            "into a clear and concise paragraph that captures the key points. "
            "Keep the summary short and useful for revision.\n\n"
            f"Study Notes:\n{text}"
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"AI summary generation failed: {str(e)}")
