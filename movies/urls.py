from django.urls import path
from . import views

app_name='movies'
urlpatterns =[ 
    #/movies/
    path("", views.index, name='index'),
    #/movies/id
    path('<int:movie_id>/', views.show, name='show'),
    ]