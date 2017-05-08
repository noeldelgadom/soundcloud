from django.shortcuts import render
from songs.models import Song
from songs.forms import NewSongForm
import songs.templates

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    song_list = Song.objects.order_by('track_name')
    return render(request, 'songs_index.html', {'songs': song_list})

def new(request):
    form = NewSongForm()
    return render(request, 'songs_new.html', {'form':form})
