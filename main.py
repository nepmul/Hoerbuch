import requests
from epub2txt import epub2txt

"""
CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/alMSnmMfBQWEfTP8MRcX"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "971662cf6e00425c0e7dc507397ad586"
}

data = {
  "text": "Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks and podcasts",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
"""

res = epub2txt("ebook.epub", outputlist=True)

for e, i in enumerate(res):
    with open(f"book{e}.txt", "w") as f:
            f.write(i)