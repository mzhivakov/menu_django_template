from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base.html")

def menu_handler(request, url_path):
    return render(request, "base.html")