# SmartNotes- AI-Powered Study Assistant

SmartNotes is a web application that helps students organize their study notes and generate AI-powered summaries to improve learning efficiency. Users can input study material, store it in a database, and use Google Gemini to generate concise summaries of their content.

## Live URL

 *https://smartnotes-oqjo.onrender.com*

## Features

- **Add Study Notes** - Enter and save study notes through a simple web interface
- **View Notes** - Browse all previously saved notes with timestamps
- **Delete Notes** - Remove notes that are no longer needed
- **AI Summarization** *(AI-Powered)* - Generate concise summaries of study notes using Google Gemini
- **Persistent Storage** - All notes are stored in MongoDB for reliable data persistence

## Architecture

```
User Browser
     |
     v
 Flask App (app.py)
     |
     |--- /            --> Render index.html with all notes
     |--- /health      --> JSON health check
     |--- /notes       --> Save new note to MongoDB
     |--- /delete/<id> --> Remove note from MongoDB
     |--- /summarize/<id> --> Call Gemini API, save summary
     |
     +--- config.py    --> Load environment variables
     +--- db.py        --> MongoDB connection (Atlas)
     +--- ai.py        --> Gemini REST API integration
     |
     v
 MongoDB Atlas          Google Gemini REST API
 (notes collection)     (summarization)
```

### System Layers

| Layer | Component | Description |
|-------|-----------|-------------|
| Presentation | HTML + CSS (templates/) | User interface with forms and note display |
| Application | Flask routes (app.py) | Handles HTTP requests and responses |
| Business Logic | ai.py | Gemini REST API integration for summarization |
| Persistence | db.py + MongoDB Atlas | Data storage and retrieval |

## Tech Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| Backend | Python + Flask | Lightweight and easy to develop with; well-suited for a 3-week project |
| Database | MongoDB Atlas | Free tier available; flexible document model fits our note structure |
| Frontend | HTML + CSS | Simple and effective; no framework overhead needed |
| AI / LLM | Google Gemini 2.5 Flash Lite (REST API) | API key provided by instructor; called via Vertex AI REST endpoint |
| CI/CD | GitHub Actions | Course standard; integrates directly with our repository |
| Deployment | Render | Free tier with deploy hooks; supports automatic deployment |
| Containerization | Docker + gunicorn | Production-ready WSGI server for reliable deployment |

## CI/CD Pipeline

```
git push to main
       |
       v
  GitHub Actions CI
  (lint + test + Docker build + smoke test)
       |
       v
  GitHub Actions CD
  (lint + test + triggers Render deploy hook)
       |
       v
  Render auto-deploys
  (pulls latest, builds Docker, starts container with gunicorn)
       |
       v
  Live at public URL
```

## Team Members

| Member | Role | Ownership Area |
|--------|------|---------------|
| Member 1 | Backend Developer + AI Integration | Flask routes, MongoDB connection, Gemini API integration |
| Member 2 | Frontend Developer + DevOps | HTML/CSS templates, Dockerfile, CI/CD pipelines, Render deployment |

## Project Timeline

| Week | Goals |
|------|-------|
| Week 11 | Project setup, Flask skeleton, MongoDB connection, Dockerfile, README proposal |
| Week 12 | Core features (CRUD notes, AI summaries), unit tests (15+), CI pipeline |
| Week 13 | CD pipeline, Render deployment, UI polish, presentation prep |

## Setup Instructions

### Prerequisites
- Python 3.11+
- MongoDB Atlas account (or local MongoDB)
- Google Gemini API key

### Local Development

```bash
# Clone the repository
git clone https://github.com/AhmadAlhitmi/projectINFS3203
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

### Running Tests

```bash
pytest tests/ -v
```

Visit `http://localhost:5000` in your browser.

## License

This project was created for INFS3203 - Systems Deployment & Implementation at the University of Doha for Science & Technology (Winter 2026).
