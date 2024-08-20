import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr

# Set up Spotify credentials
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
                                               client_secret=os.getenv('CLIENT_SECRET'),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public"))


# Function to search for a song and add it to a playlist
def add_song_to_playlist(song_name, playlist_name):
    # Search for the song
    results = sp.search(q=song_name, limit=1)

    # Get the first search result (assuming it's the song you want)
    track_uri = results['tracks']['items'][0]['uri']

    # Find or create the playlist
    playlists = sp.current_user_playlists()
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
            break
    if not playlist_id:
        new_playlist = sp.user_playlist_create(sp.me()['id'], playlist_name)
        playlist_id = new_playlist['id']

    # Add the song to the playlist
    sp.playlist_add_items(playlist_id, [track_uri])
# Python program to translate
# speech to text and text to speech


def convert_spoken_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:
        print("Please speak:")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture spoken words
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


# Main program
if __name__ == "__main__":
    # Get song name and playlist name from user input
    song_name = convert_spoken_to_text()
    # song_name = input('enter the song: ')
    print(song_name)
    playlist_name = "devotional"

    # Add the song to the playlist
    add_song_to_playlist(song_name, playlist_name)
