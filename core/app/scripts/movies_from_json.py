import json
from app.models import Movie
import os

print(os.getcwd())
def import_movies_from_json(file_path):
    print(os.getcwd())
    with open('/home/nik/Рабочий стол/django_exam/core/movies.json', 'r') as file:
        movies_data = json.load(file)

        for movie_data in movies_data:
            movie = Movie(
                title=movie_data['title'],
                year=movie_data['year'],
                cast=', '.join(movie_data['cast']),
                genres=', '.join(movie_data['genres']),
                href=movie_data.get('href', ''),
                extract = movie_data.get('extract', ''),
                thumbnail = movie_data.get('thumbnail', ''),
                thumbnail_width=movie_data.get('thumbnail_width', 0),
                thumbnail_height=movie_data.get('thumbnail_height', 0),
            )
            movie.save()