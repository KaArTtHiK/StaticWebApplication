from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('gallery',views.gallery, name = 'gallery'),
    path('blog',views.blog, name = 'blog'),
    path('contact',views.contact, name = 'contact'),
    path('blog-single-post', views.blog_single_post,name = 'blog-single-post'),
    path('gallery-single-post', views.gallery_single_post, name = 'gallery-single-post')

]