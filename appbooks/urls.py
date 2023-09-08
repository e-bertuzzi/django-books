from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.readings_list, name="home"),
    path("home/book/<int:pk>", views.book, name="book"),
    path("home/book/<int:pk>/autore/<int:pk2>", views.author, name="author")
]