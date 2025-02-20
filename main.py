import requests
from epub2txt import epub2txt
from os import mkdir


ebook_name="Buch.epub"

max_characters = 1000

characters={

    "Ã¼": "ü",
    "Ã¤": "ä",
    "Ã¶": "ö",
    "Ã": "ß",
    "â": "'"#muss an letzter stelle stehen, da nur ein zeichen
}


CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/XXX"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "XXX"
}

book_dir=ebook_name.split(".")[0]
try:
    mkdir(book_dir)
except:
    pass



ebook = epub2txt(ebook_name, outputlist=False)

for key in characters:
    ebook=ebook.replace(key, characters[key])



sentences=ebook.split(".")

sections=[""]
for i in sentences:
    if len(sections[-1]) + len(i) >= max_characters -1:
        sections.append("")
    sections[-1]+=i+". "


for e, i in enumerate(sections):
    if len(i) > max_characters:
        print(f"Section too long: {len(i)} > {max_characters} \n {i}")

if input(f"{e} sections, commit? (Y)") != "Y":
    quit()


for e, i in enumerate(sections):

    data = {
      "text": i,
      "model_id": "eleven_multilingual_v2",
      "voice_settings": {
        "stability": 1,
        "similarity_boost": 1
      }
    }

    print(f'{book_dir}/{book_dir}_{e}')


    response = requests.post(url, json=data, headers=headers)
    with open(f'{book_dir}/{book_dir}_{e}', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

