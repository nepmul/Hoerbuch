import requests
from epub2txt import epub2txt

max_characters = 500

characters={

    "Ã¼": "ü",
    "Ã¤": "ä",
    "Ã¶": "ö",
    "Ã":"ß",    #muss an letzter stelle stehen, da nur ein zeichen
}


CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/FVQMzxJGPUBtfz1Azdoy"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "971662cf6e00425c0e7dc507397ad586"
}






ebook = epub2txt("ebook.epub", outputlist=False)

for key in characters:
    ebook=ebook.replace(key, characters[key])



sentences=ebook.split(".")

sections=[""]
for i in sentences:
    if len(sections[-1]) + len(i) >= max_characters:
        sections.append("")
    sections[-1]+=i+". "



for e, i in enumerate(sections):

    data = {
      "text": i,
      "model_id": "eleven_multilingual_v2",
      "voice_settings": {
        "stability": 1,
        "similarity_boost": 1
      }
    }

    print(i)
    print(len(i))


    response = requests.post(url, json=data, headers=headers)
    with open(f'Testbuch_{e}', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)