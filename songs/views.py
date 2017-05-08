from django.shortcuts import render
from songs.models import Song
import songs.templates

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    song_list = Song.objects.order_by('track_name')
    return render(request, 'songs_index.html', {'songs': song_list})
