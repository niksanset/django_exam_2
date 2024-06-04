from django.core.management.base import BaseCommand
from app.scripts.movies_from_json import import_movies_from_json
class Command(BaseCommand):
    help = 'Imports movies from JSON file into the database'

    def handle(self, *args, **options):
        file_path = '/scripts/movies.json'
        import_movies_from_json(file_path)
        self.stdout.write(self.style.SUCCESS('Movies imported successfully!'))