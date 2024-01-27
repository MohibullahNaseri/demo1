from django.urls import path
from . import views

urlpatterns = [
    path('portfolio', views.portfolio, name='portfolio'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
]