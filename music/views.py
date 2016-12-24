from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums = Album.objects.all() #This will connect to the database nd will provide all of the albums
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: " + str(album_id) + "</h2>")

