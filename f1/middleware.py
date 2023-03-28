from datetime import date
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse

#caches the season
class SeasonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #---------------get_season function-------------------
        season = request.session.get('season', int(date.today().year))
        selected_season = request.GET.get('selected_season')

        if selected_season and selected_season != season:
            request.session['season'] = int(selected_season)
            season = selected_season
        #-----------------return season----------------------

        #------------------cache-key-func----------------------
        # Get the current season from the global variable or request.session
        current_season = request.session.get('season', int(date.today().year))

        # Get the cache key for the current request
        cache_key = self.get_cache_key(request)

        # Check if the cached season matches the current season
        if cache_key:
            cached_season = cache.get('season_cache_key')
            if cached_season and cached_season != current_season:
                # Clear the cache if the season has changed
                cache.delete(cache_key)
        
        # Process the request and get the response
        response = self.get_response(request)

        # Set the cached season if it's not already set
        if not cache.get('season_cache_key'):
            cache.set('season_cache_key', current_season)

        return response

    def get_cache_key(self, request):
        # Build the cache key for the current request
        cache_key = 'views.decorators.cache.cache_page.%s.%s.%s.%s.%s' % (
            request.method,
            request.get_host(),
            request.path,
            request.GET.urlencode(),
            settings.CACHE_MIDDLEWARE_KEY_PREFIX,
        )
        return cache_key