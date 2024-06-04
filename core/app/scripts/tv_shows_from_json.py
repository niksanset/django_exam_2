import json
from app.models import TVShow


def import_tv_shows_from_json(file_path):
    with open('/Users/mac/Downloads/django_exam/core/tv-shows.json', 'r') as file:
        tv_shows_data = json.load(file)

        for tv_show_data in tv_shows_data:
            tv_show = TVShow(
                name=tv_show_data.get('name', ''),
                language=tv_show_data.get('language', ''),
                genres=', '.join(tv_show_data.get('genres', [])),
                status=tv_show_data.get('status', ''),
                runtime=tv_show_data.get('runtime', 0),
                average_rating=tv_show_data.get('rating', {}).get('average', 0),
                premiered=tv_show_data.get('premiered', ''),
                ended=tv_show_data.get('ended', ''),
                official_site=tv_show_data.get('officialSite', ''),
                summary=tv_show_data.get('summary', ''),
                imdb_id=tv_show_data.get('externals', {}).get('imdb', ''),
                image_medium=tv_show_data.get('image', {}).get('medium', ''),
                image_original=tv_show_data.get('image', {}).get('original', '')
            )
            tv_show.save()