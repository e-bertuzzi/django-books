from datetime import date, datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from appbooks.models import Reading, Author

# Create your views here.

@login_required(login_url="/login/")
def readings_list(request):
    today_seconds = datetime.today().timestamp() #positivo
    readings = Reading.objects.all()
    return render(request, 'readings_list.html', {'readings': readings, 'today_seconds': today_seconds})

@login_required(login_url="/login/")
def book(request, pk):
    reading = Reading.objects.get(pk=pk)
    return render(request, 'book.html', {'reading': reading})

@login_required(login_url="/login/")
def author(request, pk, pk2):
    reading = Reading.objects.get(pk=pk)
    author = Author.objects.get(pk=pk2)
    return render(request, 'author.html', {'author': author, 'reading': reading})