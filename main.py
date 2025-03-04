from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Error: Could not request results. Check your internet connection.")
        return None

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Windows ke liye, Linux/mac ke liye 'mpg321 response.mp3'

if __name__ == "__main__":
    command = recognize_speech()
    if command:
        speak(f"You said: {command}")

