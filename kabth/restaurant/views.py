from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import BookingForm

def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, 'about.html')
def menu(request):
    menu_contents = models.Menu.objects.all()
    return render(request, 'menu.html',{"menu":menu_contents})
def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"booking.html",{"form":form})
def menu_item(request, pk=None):
    if pk:
        menu_item = models.Menu.objects.get(pk = pk)
    else:
        menu_item=""
    return render(request,"menu_item.html",{"menu_item":menu_item})