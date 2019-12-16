from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def home(request):
   images = Image.get_all()
   
   return render(request, 'gal/home.html', {'images':images})