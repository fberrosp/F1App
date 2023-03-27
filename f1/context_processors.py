from .services import get_api_data


def seasons(request):
    seasons = get_api_data('seasons')['SeasonTable']['Seasons']

    return {'seasons': sorted(seasons, key=lambda d: d['season'], reverse=True)}