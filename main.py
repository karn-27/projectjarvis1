from flask import Flask, request, jsonify
import speech_recognition as sr
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

# 🎤 Speech Recognition (Fixed: Accept Audio File Instead of Mic)
@app.route("/listen", methods=["POST"])
def listen():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    audio_path = "uploaded_audio.wav"
    audio_file.save(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return jsonify({"message": "Speech recognized", "text": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except sr.RequestError:
        return jsonify({"error": "Speech recognition request failed"}), 500

# 🔊 Text-to-Speech (Same as Before)
@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")

    return jsonify({"message": "Speech generated!", "file": "response.mp3"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
