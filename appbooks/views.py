from datetime import date, datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from appbooks.models import Reading, Author

# Create your views here.

@login_required(login_url="/login/")
def readings_list(request):
    order_by = request.GET.get('order_by')
    if order_by is None:
        order_by = 'data_inizio'

    today_seconds = datetime.today().timestamp() #positivo

    if order_by == 'titolo':
        readings = Reading.objects.all().order_by('book__titolo')
    else:
        readings = Reading.objects.all().order_by(order_by)

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