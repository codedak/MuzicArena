from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all() #This will connect to the database nd will provide all of the albums
    #Now we create a dictionary
    context = {'all_albums' : all_albums}
    #return render(request, 'music/index.html', {'all_albums' : all_albums})  'OR'
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("This Album Does Not Exist")
    contxt = {'album' : album}
    #return render(request, 'music/index.html', {'album' : album})  'OR'
    return render(request, 'music/detail.html', contxt)

