from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Music app Homepage</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: " + str(album_id) + "</h2>")

