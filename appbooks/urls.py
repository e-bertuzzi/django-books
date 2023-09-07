from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.readings_list, name="home"),
    path("home/book/<int:pk>", views.book, name="book")
]