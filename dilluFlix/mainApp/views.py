from django.shortcuts import render

# Create your views here.
def index(request):
    pagetype={'pagetype':'Home'}
    return render(request,'index.html',context=pagetype)

def contact(request):
    pagetype={'pagetype':'Contact'}
    return render(request,'contact.html',context=pagetype)

def anime(request):
    pagetype={'pagetype':'Anime'}
    return render(request,'anime.html',context=pagetype)

def movies(request):
    pagetype={'pagetype':'Movies'}
    return render(request,'movies.html',context=pagetype)

class player():

    class anime():
        def yourname(request):
            pagetype= {'pagetype':'Anime',
            'vlink':'https://www.googleapis.com/drive/v3/files/1gMQzyUxPwsRj9TYR8c-84c7h9yHsbPhw?alt=media&key=AIzaSyC7yLFQ12QAndpdRXweN-0JYUCvhqn7GBc'
            ,'slink':'static/anime/subs/yourname.vtt'}
            return render(request,'player.html',context=pagetype)