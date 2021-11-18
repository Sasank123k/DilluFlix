from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('', views.index),
    path('index',views.index),
    path('contact',views.contact),
    path('anime',views.anime),
    path('movies',views.movies),
    path('yourname',views.player.anime.yourname)
]