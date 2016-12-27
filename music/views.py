from django.views import generic
from .models import Album

class IndexView(request.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(request.DetailView):
    model = Album
    template_name = 'music/detail.html'