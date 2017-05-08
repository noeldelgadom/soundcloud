from django.shortcuts import render
import albums.templates

# Create your views here.
def index(request):
    return render(request, 'albums_index.html')
