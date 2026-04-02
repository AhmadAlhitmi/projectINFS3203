# SmartNotes - AI-Powered Study Assistant

SmartNotes is a web application that helps students organize their study notes and generate AI-powered summaries to improve learning efficiency. Users can input study material, store it in a database, and use Google Gemini to generate concise summaries of their content.

## Features

- **Add Study Notes** - Enter and save study notes through a simple web interface
- **View Notes** - Browse all previously saved notes with timestamps
- **Delete Notes** - Remove notes that are no longer needed
- **AI Summarization** *(AI-Powered)* - Generate concise summaries of study notes using Google Gemini
- **Persistent Storage** - All notes are stored in MongoDB for reliable data persistence

## Tech Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| Backend | Python + Flask | Lightweight and easy to develop with; well-suited for a 3-week project |
| Database | MongoDB Atlas | Free tier available; flexible document model fits our note structure |
| Frontend | HTML + CSS | Simple and effective; no framework overhead needed |
| AI / LLM | Google Gemini 2.5 Flash | API key provided by instructor; strong summarization capabilities |
| CI/CD | GitHub Actions | Course standard; integrates directly with our repository |
| Deployment | Render | Free tier with deploy hooks; supports automatic deployment |
| Containerization | Docker | Required for the project; ensures consistent environments |

## Team Members

| Member | Role | Ownership Area |
|--------|------|---------------|
| Ahmad Alhitmi | Backend Developer + AI Integration | Dockerfile, MongoDB connection, Gemini API integration |
| Mohammed Almarwani | Frontend Developer + DevOps | HTML/CSS templates, Flask routes, CI/CD pipelines, Render deployment |

## Project Timeline

| Week | Goals |
|------|-------|
| Week 11 | Project setup, Flask skeleton, MongoDB connection, Dockerfile, README proposal |
| Week 12 | Core features (CRUD notes, AI summaries), unit tests (12+), CI pipeline |
| Week 13 | CD pipeline, Render deployment, UI polish, presentation prep |

## Setup Instructions

### Prerequisites
- Python 3.11+
- MongoDB Atlas account (or local MongoDB)
- Google Gemini API key

### Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/smartnotes.git
cd smartnotes

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your MongoDB URI and Gemini API key

# Run the application
python app.py
```

### Docker

```bash
# Build the image
docker build -t smartnotes .

# Run the container
docker run -p 5000:5000 --env-file .env smartnotes
```

Visit `http://localhost:5000` in your browser.

## Live URL

*Coming in Week 13 after Render deployment*

## License

This project was created for INFS3203 - Systems Deployment & Implementation at the University of Doha for Science & Technology (Winter 2026).
