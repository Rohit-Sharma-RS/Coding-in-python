from bs4 import BeautifulSoup
import requests
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12/")

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
for song in song_names_spans:
    print(song.get_text().strip())
