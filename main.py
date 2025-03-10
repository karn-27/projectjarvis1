from flask import Flask, request, jsonify
import speech_recognition as sr
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")

    return jsonify({"message": "Speech generated!", "file": "response.mp3"})

@app.route("/listen", methods=["GET"])
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
        return jsonify({"error": "Sorry, I could not understand the audio."}), 400
    except sr.RequestError:
        return jsonify({"error": "Could not request results. Check your internet connection."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default port
    app.run(host="0.0.0.0", port=port)
