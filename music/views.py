from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Music app Homepage</h1>")