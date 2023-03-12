import requests


def get_movie(name="matrix") -> dict:
    movie_data = requests.get(f"https://www.omdbapi.com/?apikey=f2056e05&t={name}")
    return movie_data.json()


movie = get_movie('titanic')
print(movie)
