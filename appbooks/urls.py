from django.urls import path
from . import views

urlpatterns = [
    path("", views.readings_list, name="home"),
    path("book/<int:pk>", views.book, name="book")
]