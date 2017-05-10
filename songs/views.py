from django.shortcuts import render
from songs.models import Song
from songs.forms import NewSongForm
import songs.templates

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    song_list = Song.objects.all()
    return render(request, 'songs_index.html', {'songs': song_list})

def new(request):
    form = NewSongForm()
    if request.method == 'POST':
        form = NewSongForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: form invalid')
    else:
        return render(request, 'songs_new.html', {'form':form})
