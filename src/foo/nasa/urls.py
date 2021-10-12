from django.urls import path
from django.contrib import admin
from django.urls import path
from foo.nasa import views as nasa_views
from . import views

urlpatterns = [
    path('', views.homepage, name='nasa'),
    path('pod/', views.picture_of_day, name='pod'),
    path('listpods/', views.photo_list, name='listpods' ),
    path('createpod/', views.photo_form, name='createpod' ),
    path('create/', views.CreateView.as_view(), name='create')
]