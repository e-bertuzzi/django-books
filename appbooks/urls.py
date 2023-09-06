from django.urls import path
from . import views

urlpatterns = [
    path("", views.readings_list, name="home"),
    path("book/<str:titolo>", views.book, name="book")
]