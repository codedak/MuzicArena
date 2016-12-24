from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all() #This will connect to the database nd will provide all of the albums
    template = loader.get_template('music/index.html')
    #Now we create a dictionary
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: " + str(album_id) + "</h2>")

