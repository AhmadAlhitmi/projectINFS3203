from pymongo import MongoClient
from config import MONGO_URI

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client.smartnotes
    notes_collection = db.notes
except Exception:
    client = None
    db = None
    notes_collection = None