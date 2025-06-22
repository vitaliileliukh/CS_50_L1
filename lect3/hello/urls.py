from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.greet, name='greet'),
    path("vitalii", views.vitalii, name='vitalii'),
    path("sasha", views.sasha, name='sasha'),
]