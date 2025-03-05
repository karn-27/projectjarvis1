import requests
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am Jarvis AI!"

# ✅ Koyeb ki URL se API test karne ka function
def test_api():
    url = "https://your-koyeb-url.com"  # अपनी Koyeb URL डालो
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

# ✅ Server start karne ka function
if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
    test_api()
