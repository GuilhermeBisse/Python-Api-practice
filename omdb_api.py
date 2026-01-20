import requests
from PIL import Image

apikey = '********'

name = input("Digite o nome do filme/série: ")

name_modified = name.split()
name_modified = "-".join(name_modified).capitalize()

url = f'http://www.omdbapi.com/?t={name}&apikey={apikey}'

response = requests.get(url)
response.raise_for_status()

data = response.json()

poster_url = data['Poster']
poster_content = requests.get(poster_url).content

with open(f'posters/poster_{name_modified}.jpg', 'wb') as file:
    file.write(poster_content)
