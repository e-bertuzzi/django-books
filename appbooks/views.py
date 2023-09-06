from django.shortcuts import render

from appbooks.models import Reading

# Create your views here.

#def index(request):
#    return render(request, 'index.html')

def readings_list(request):
    readings = Reading.objects.all()
    return render(request, 'readings_list.html', {'readings': readings})

def book(request, pk):
    reading = Reading.objects.get(pk=pk)
    return render(request, 'book.html', {'reading': reading})