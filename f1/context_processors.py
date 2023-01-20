from .services import get_api_data
from datetime import date


def seasons(request):
    seasons = get_api_data('seasons')['SeasonTable']['Seasons']
    request.session['season'] = int(date.today().year)

    return {'seasons': sorted(seasons, key=lambda d: d['season'], reverse=True)}
