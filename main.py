from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import os
from gtts import gTTS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Allow all origins

# ✅ Ensure "static" directory exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

# 🔊 Text-to-Speech Route
@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    file_path = os.path.join("static", "response.mp3")

    # ✅ Save the file in "static" folder
    tts = gTTS(text=text, lang="en")
    tts.save(file_path)

    return jsonify({"message": "Speech generated!", "file": "/static/response.mp3"})

# ✅ New Route to Serve MP3 File
@app.route("/static/<filename>")
def serve_audio(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
