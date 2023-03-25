import json
import requests
from decouple import config
from django.shortcuts import redirect, render
from models.movies import Movie
from django.http import JsonResponse



def tmdb_api(quest: str = 'discover', order: str = 'movie', params: dict = {}):
    STATIC_URL = f'https://api.themoviedb.org/3/{quest}/{order}'
    API_KEY = config('API_KEY')
    params['api_key'] = API_KEY
    params['language'] = 'es-MX'
    request = requests.get(STATIC_URL, params=params)
    
    return requests.get(STATIC_URL, params=params)


def movies_json(request):
    try:
        movies_request = tmdb_api(params={'sort_by': 'popularity.desc','language' : 'es-MX'})
        movies = [Movie(movie).to_dict()
                        for movie in movies_request.json()['results']]
    except:
        movies = {'Error': 'Not found'}
    
    return JsonResponse(movies[:10],safe=False)

def index(request):
    movies= movies_json(request).content.decode("ANSI")
    context = {'movies': json.loads(movies)}
    return render(request, 'index.html', context)


def get_video(request, id):
    quest = f'movie/{id}'
    order = 'videos'
    try:
        movie_request = tmdb_api(quest=quest,order=order)
        movie_trailer = {'key':movie_request.json()['results'][0]['key'],
                         'name':movie_request.json()['results'][0]['name']}
    except:
        movie_trailer = {'Error': 'Not found'}

    return JsonResponse(movie_trailer)
