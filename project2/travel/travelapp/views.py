from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def blog_single_post(request):
    return render(request, 'blog-single-post.html')

def gallery_single_post(request):
    return render(request, 'gallery-single-post.html')
