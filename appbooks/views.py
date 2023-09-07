from datetime import date, datetime
from django.shortcuts import render

from appbooks.models import Reading

# Create your views here.

def readings_list(request):
    today_seconds = datetime.today().timestamp() #positivo
    readings = Reading.objects.all()
    return render(request, 'readings_list.html', {'readings': readings, 'today_seconds': today_seconds})

def book(request, pk):
    reading = Reading.objects.get(pk=pk)
    return render(request, 'book.html', {'reading': reading})