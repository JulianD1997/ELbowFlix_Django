import json
import requests
from decouple import config
from django.shortcuts import redirect, render
from models.movies import Movie


quest = 'discover'
order = 'movie'
""" constants variables """
STATIC_URL = f'https://api.themoviedb.org/3/{quest}/{order}'
API_KEY = config('API_KEY')

params = {'api_key':API_KEY,
          'language':'es',
          'sort_by':'popularity.desc'
          }
def movies_json(request):
    try:
        movies_request = requests.get(STATIC_URL,params=params)
        movies=[Movie(movie).to_dict() for movie in movies_request.json()['results']]
    except:
        movies = {'Error':'Not found'}
    
    return json.dumps(movies)

def index(request):
    context = {'movies' : json.loads(movies_json(request))[:10]}
    return render(request,'index.html',context)


    
    

         