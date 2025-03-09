import requests

KOYEB_URL = "https://hilarious-dolley-karna-2c72694d.koyeb.app"  # Replace with your Koyeb App URL

def test_listen():
    print("Testing Speech Recognition API...")
    response = requests.get(f"{KOYEB_URL}/listen")
    print(response.json())

def test_speak():
    print("Testing Text-to-Speech API...")
    response = requests.post(f"{KOYEB_URL}/speak", json={"text": "Hello, I am Jarvis AI!"})
    print(response.json())

if __name__ == "__main__":
    test_listen()
    test_speak()
