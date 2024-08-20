import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os


birdy_uri = os.getenv('BIRDY_URI')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
