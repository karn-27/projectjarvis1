from flask import Flask, request, jsonify
import speech_recognition as sr
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

# 🎤 Speech Recognition Route
@app.route("/listen", methods=["POST"])
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return jsonify({"message": "Speech recognized", "text": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand audio"}), 400
    except sr.RequestError:
        return jsonify({"error": "Speech recognition request failed"}), 500

# 🔊 Text-to-Speech Route
@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("start response.mp3")  # Windows ke liye, Linux/mac ke liye 'mpg321 response.mp3'
    
    return jsonify({"message": "Speech generated!", "file": "response.mp3"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
