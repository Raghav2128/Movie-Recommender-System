import os
import requests

def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Download similarity.pkl from Google Drive if not present
if not os.path.exists("similarity.pkl"):
    print("Downloading similarity.pkl from Google Drive...")
    download_file_from_google_drive("1mujwvz2QlxdsVzhdqN7GrAJyjUv2K7NR", "similarity.pkl")
    print("Download complete.")

# Download tmdb_5000_credits.csv from Google Drive if not present
if not os.path.exists("tmdb_5000_credits.csv"):
    print("Downloading tmdb_5000_credits.csv from Google Drive...")
    download_file_from_google_drive("1yn4JI5pU1I7-wEKNMYGUHK8_hvEP-S4t", "tmdb_5000_credits.csv")
    print("Download complete.") 