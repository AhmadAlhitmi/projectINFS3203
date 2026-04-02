from flask import Flask, jsonify
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def home():
    return "Welcome to SmartNotes!"


@app.route("/health")
def health():
    """Health check endpoint for container monitoring."""
    return jsonify({"status": "healthy", "app": "SmartNotes"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
