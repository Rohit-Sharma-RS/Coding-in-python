from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')

movie_names = soup.find_all(name='h3', class_="listicleItem_listicle-item__title__BfenH")
all_movies = [movie_name.get_text() for movie_name in movie_names]


with open('movies.txt', 'w') as file:
    for movie in reversed(all_movies):
        file.write(f'{movie}\n')



