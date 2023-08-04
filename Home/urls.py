from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about),
    path('projects/', views.projects,name='projects'),
    path('contact/', views.contact,name='contact')
]