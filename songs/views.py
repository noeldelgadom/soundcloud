from django.shortcuts import render
import songs.templates

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'songs_index.html')
