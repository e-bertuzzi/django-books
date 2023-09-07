from datetime import date
from django.shortcuts import render

from appbooks.models import Reading

# Create your views here.

def readings_list(request):
    today = date.today();
    readings = Reading.objects.all()
    return render(request, 'readings_list.html', {'readings': readings, 'today': today})

def book(request, pk):
    reading = Reading.objects.get(pk=pk)
    return render(request, 'book.html', {'reading': reading})