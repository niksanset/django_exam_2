from django.core.management.base import BaseCommand
from app.scripts.tv_shows_from_json import import_tv_shows_from_json
class Command(BaseCommand):
    help = 'Imports tv shows from JSON file into the database'

    def handle(self, *args, **options):
        file_path = 123
        import_tv_shows_from_json(file_path)
        self.stdout.write(self.style.SUCCESS('Tv shows imported successfully!'))