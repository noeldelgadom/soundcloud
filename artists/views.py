from django.shortcuts import render
import artists.templates

# Create your views here.
def index(request):
    return render(request, 'artists_index.html')
