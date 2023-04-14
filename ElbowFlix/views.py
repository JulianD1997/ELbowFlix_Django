import json

import requests
from decouple import config
from django.http import JsonResponse
from django.shortcuts import redirect, render

from models.movies import Movie


def get_trailer(movie_request):
    """
    Busca el tráiler de la película en la respuesta de la API de TMDB.
    Retorna un diccionario con la clave 'key' y el valor del ID del video, y
    la clave 'name' y el valor del nombre del video.
    """
    for result in movie_request.json()["results"]:
        if result.get("type") == "Trailer":
            return {"key": result.get('key'), "name": result.get("name")}

    return {}


def tmdb_api(resource: str = "discover", type_: str = "movie", params: dict = {}):
    """
    Realiza una llamada a la API de TMDB y retorna la respuesta.
    Si la llamada falla, retorna un diccionario vacío.
    """
    STATIC_URL = f"https://api.themoviedb.org/3/{resource}/{type_}"
    API_KEY = config("API_KEY")
    params["api_key"] = API_KEY
    params.setdefault("language", "es-MX")
    params = dict(sorted(params.items(), key=lambda x: x[1]))
    response = requests.get(STATIC_URL, params=params)
    response.raise_for_status()
    #print(response.url)
    return response


def get_video(request, id):
    """
    Obtiene el tráiler de una película a partir de su ID.
    Retorna un objeto JSON con el ID y nombre del tráiler.
    Si no se encuentra un tráiler, retorna un objeto JSON vacío.
    """
    resource = f"movie/{id}"
    type_ = "videos"
    languages = ["es-MX", "es-ES", "en-US"]

    for language in languages:
        try:
            movie_request = tmdb_api(resource=resource, type_=type_, params={
                                     "language": language})
            movie_trailer = get_trailer(movie_request)
            if movie_trailer:
                return JsonResponse(movie_trailer)
        except requests.exceptions.HTTPError as e:
            pass

    # Si no se encontró un tráiler, devuelve un objeto JSON vacío
    return JsonResponse({'Error': 'no found'})


def index(request):
    """
    Renderiza la página principal con una lista de películas.
    """
    movies = movies_json(request).content.decode("utf-8")
    context = {"movies": json.loads(movies)}

    return render(request, "index.html", context)


def movies_json(request):
    """
    Obtiene una lista de las 10 películas más populares de TMDB.
    Retorna un objeto JSON con información de cada película.
    Si no se puede obtener la lista, retorna un objeto JSON vacío.
    """
    params = {}
    try:
        if not len(request.GET):
            params["sort_by"] = "popularity.desc"
            movies_request = tmdb_api(
                params=params
            )
            movies = [
                Movie(movie).to_dict() for movie in movies_request.json()['results'][:10]
            ]
            return JsonResponse(movies, safe=False)
        
        resource = request.GET.get('resource')
        type_ = request.GET.get('type_')
        
        if type_ == 'upcoming':
            params['region'] = request.GET.get('region')
            params['language'] = 'es-ES'
            
        movies_request = tmdb_api(
            resource=resource,
            type_=type_,
            params=params
        )
        movies = [
            Movie(movie).to_dict() for movie in movies_request.json()['results']
        ]
    except Exception as e:
        print(e)
        movies = {"Error": "No found"}
    return JsonResponse(movies, safe=False)
