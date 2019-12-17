from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Category

# Create your views here.
def home(request):
   images = Image.get_all()
   
   return render(request, 'gal/home.html', {'images':images})

def search_results(request):
   if 'category' in request.GET and request.GET["category"]:
      search_term = request.GET.get("category")
      searched_images = Image.search_image(search_term)
      message = f"{search_term}"

      return render(request, 'gal/search.html',{"message":message, "images":searched_images})

   else:
      message = "You haven't searched for any term"
      return render(request, 'gal/search.html',{"message":message})