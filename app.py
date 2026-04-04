from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from config import SECRET_KEY
from db import notes_collection
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def home():
    """Display all saved notes, newest first."""
    notes = list(notes_collection.find().sort("created_at", -1))
    return render_template("index.html", notes=notes)


@app.route("/health")
def health():
    """Health check endpoint for container monitoring."""
    return jsonify({"status": "healthy", "app": "SmartNotes"}), 200


@app.route("/notes", methods=["POST"])
def add_note():
    """Save a new study note to the database."""
    text = request.form.get("text", "").strip()

    if not text:
        flash("Note cannot be empty.", "error")
        return redirect(url_for("home"))

    note = {
        "text": text,
        "created_at": datetime.utcnow(),
        "summary": None
    }
    notes_collection.insert_one(note)
    flash("Note saved successfully!", "success")
    return redirect(url_for("home"))


@app.route("/delete/<note_id>", methods=["POST"])
def delete_note(note_id):
    """Delete a note from the database by its ID."""
    try:
        result = notes_collection.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 1:
            flash("Note deleted.", "success")
        else:
            flash("Note not found.", "error")
    except Exception:
        flash("Invalid note ID.", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
