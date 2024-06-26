from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movies]

# Reverse list
movies = movie_titles[::-1]

#for n in range(len(movie_titles)-1, -1, -1):
#   print(movie_titles[n])

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")
