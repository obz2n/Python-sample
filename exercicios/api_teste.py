# %%
import requests
import pandas as pd
import json

# -- Constantes --

LIMITE = 100

# -- Funções auxiliares --

# Função para obter os dados da API
url = "https://api.artic.edu/api/v1/artworks"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:    print(f"Error: {response.status_code}")

print("Dados da API:")
print(json.dumps(data, indent=4))


# -- Funções --

# Função para obter as obras de arte com base na paginação
def get_artworks(data, page, limit):
    all_artworks = data.get('data', [])
    return all_artworks[(page - 1) * limit : page * limit]

# Função para normalizar todos os dados das obras de arte
def normalize_artwork(artwork):
    return {
        'id': artwork.get('id'),
        'artist_id': artwork.get('artist_id'),
        'title': artwork.get('title'),
        'artist': artwork.get('artist_title'),
        'date_start': artwork.get('date_display'),
        'date_end': artwork.get('date_end'),
        'artist_display': artwork.get('artist_display'),
        'description': artwork.get('thumbnail', {}).get('alt_text'),
        'category_titles': artwork.get('category_titles'),
        'medium': artwork.get('medium_display'),
        'dimensions': artwork.get('dimensions'),
        'image_url': artwork.get('image_id')
    }
print("Obras de arte normalizadas:")
artworks = get_artworks(data, page=1, limit=LIMITE)
normalized_artworks = [normalize_artwork(artwork) for artwork in artworks]
print(json.dumps(normalized_artworks, indent=4))

# %%
# Função transformar os dados em dataframe
def create_dataframe(artworks):
    return pd.DataFrame(artworks)
print("DataFrame das obras de arte:")
df = create_dataframe(normalized_artworks)
df
