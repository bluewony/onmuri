from django.shortcuts import render
from .models import Home, Photo

# Create your views here.
def home(request):
    return render(request, 'index.html')

def photo(request):
    photos = Photo.objects.all()
    return render(request, 'photo.html', {'photos': photos,})

def media(request):
    return render(request, 'media.html')
