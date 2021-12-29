from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('', views.index),
    path('index',views.index),
    path('about',views.about),
    path('anime',views.anime),
    path('movies',views.movies),
    path('random',views.random),
    path('test',views.test),
    path('yourname',views.player.anime.yourname),
    path('tenkinoko',views.player.anime.tenkinoko),
    path('spiritedaway',views.player.anime.spiritedaway),
    path('hotarubi',views.player.anime.hotarubi),
    path('demonslayer',views.player.anime.demonslayer),
    path('helloworld',views.player.anime.helloworld),
    path('garden',views.player.anime.garden),
    path('silent',views.player.anime.silent),

    path('shangchi',views.player.movie.shangchi),
    path('shershah',views.player.movie.shershah),
    path('venom',views.player.movie.venom),
    path('matrix',views.player.movie.matrix),
    path('purge',views.player.movie.purge),
    path('babysitter',views.player.movie.babysitter),
    path('platform',views.player.movie.platform),
    path('benjamin',views.player.movie.benjamin),
   
    path('songs',views.songs),
    path('games',views.games)



]