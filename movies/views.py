from django.shortcuts import render
# Create your views here.
from .models import Movie
from django.http import Http404
def index(req):
    newest_movies=Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies':newest_movies}
    return render(req, 'movies/index.html',context)
    
def show(req, movie_id):
    try:
        movie=Movie.objects.get(pk=movie_id)
    except:
        raise Http404("Movie doesn't exist")
    return render(req, 'movies/show.html', {'movie':movie})