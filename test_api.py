import requests

url = "https://your-koyeb-url.com"  # अपनी Koyeb URL डालो
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", response.text)
import os
port = int(os.getenv("PORT", 3000))
app.run(host="0.0.0.0", port=port)
