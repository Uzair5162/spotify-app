from flask import Flask, render_template, jsonify, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

rocky_url = 'spotify:artist:13ubrt8QOOCPljQ2FL1Kca'

client_credentials_manager = SpotifyClientCredentials(client_id=config.client_ID, client_secret=config.client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

results = sp.artist_albums(rocky_url, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])



if __name__ == "__main__":
    app.run(debug=True)