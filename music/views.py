from django.shortcuts import render, get_object_or_404
from .models import Album


def index(request):
    all_albums = Album.objects.all() #This will connect to the database nd will provide all of the albums
    #Now we create a dictionary
    context = {'all_albums' : all_albums}
    #return render(request, 'music/index.html', {'all_albums' : all_albums})  'OR'
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    #Instead of this --> album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})

